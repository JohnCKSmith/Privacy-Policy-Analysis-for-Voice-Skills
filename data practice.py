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
    phrases = list()
    for sent in doc.sents:
        for chunk in sent.noun_chunks:
            if chunk.root.dep_ == "nsubj":
                if chunk.root.lemma_.lower() in noun_list and chunk.root.head.lemma_.lower() in verb_list:
                    phrases.append(chunk.root.lemma_ + " " + chunk.root.head.lemma_)
            if chunk.root.dep_ == "dobj":
                if chunk.root.lemma_.lower() in noun_list and chunk.root.head.lemma_.lower() in verb_list:
                    phrases.append(chunk.root.head.lemma_ + " " + chunk.root.lemma_)
    return list(set(phrases))


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
            print(extract_phrases(description))
            print(extract_phrases(policy))
            break
        break
