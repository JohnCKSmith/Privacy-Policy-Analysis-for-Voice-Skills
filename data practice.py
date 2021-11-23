import spacy
import json
import os

verb_list = ["Access", "Ask", "Assign", "Collect", "Create", "Enter", "Gather", "Import", "Obtain", "Observe", "Organize", "Provide", "Receive", "Request", "Share", "Use", "Include", "Integrate", "Monitor", "Process", "See", "Utilize", "Retain", "Cache", "Delete", "Erase", "Keep", "Remove", "Store", "Transfer", "Communicate", "Disclose", "Reveal", "Sell", "Send", "Update", "View", "Need", "Require", "Save"]
noun_list = ["Address", "Name", "Email", "Phone", "Birthday", "Age", "Gender", "Location", "Datum", "Contact", "Phonebook", "SMS", "Call", "Profession", "Income", "Information"]

noun_list = list(map(lambda item: str(item).lower(), noun_list))
verb_list = list(map(lambda item: str(item).lower(), verb_list))


def extract_phrases(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    long_phrases = list()
    nsubj_phrases = list()
    dobj_phrases = list()
    for sent in doc.sents:
        type_1 = list()
        type_2 = list()
        for chunk in sent.noun_chunks:
            if chunk.root.dep_ == "nsubj":
                type_1.append(chunk)
            if chunk.root.dep_ == "dobj":
                type_2.append(chunk)
        nsubj_phrases.extend(type_1)
        dobj_phrases.extend(type_2)
        for chunk_1 in type_1:
            for chunk_2 in type_2:
                if chunk_1.root.head.idx == chunk_2.root.head.idx:
                    phrase = chunk_1.text + " " + chunk_1.root.head.lemma_ + " " + chunk_2.root.text
                    for conj in chunk_2.conjuncts:
                        phrase += " " + conj.text
                    long_phrases.append(phrase)
    return list(set(long_phrases)), list(set(nsubj_phrases)), list(set(dobj_phrases))


skill_intro_directory = "./data/skills_intro_pages/"
privacy_policy_directory = "./data/privacy_pages/"
policy_list = json.loads(open("./data/policy_list.txt", "r").read())
collected_policy_list = os.listdir(privacy_policy_directory)
for k, v in policy_list.items():
    if v[0]+".txt" in collected_policy_list:
        for skill_intro in v:
            skill_intro_page = json.loads(open(skill_intro_directory+skill_intro+".json", "r").read())
            description = skill_intro_page['description']
            policy = open(privacy_policy_directory+v[0]+".txt", "r").read()
            print(extract_phrases(description)[0])
            print(extract_phrases(policy)[0])
            break
        break
