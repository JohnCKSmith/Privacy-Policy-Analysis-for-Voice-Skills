import spacy
import os

collect_verb = ["access", "ask", "assign", "collect", "create", "enter", "gather", "import", "need", "obtain", "observe", "organize", "provide", "receive", "request", "share", "know", "understand"]
user_verb = ["access", "include", "integrate", "monitor", "process", "see", "use", "utilize"]
retain_verb = ["cache", "delete", "erase", "keep", "remove", "retain", "store"]


def extract_phrases(target_verb_set, text):
    text = text.lower()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    root_verbs = list()
    objects = dict()
    durations = dict()
    reasons = dict()

    for sent in doc.sents:
        for token in sent:
            print(token, token.dep_, token.head)
            if token.pos_ == "VERB" and token.lemma_ in target_verb_set:
                root_verbs.append(token)
                if token not in objects.keys():
                    objects[token] = []
                if token not in durations.keys():
                    durations[token] = []
                if token not in reasons.keys():
                    reasons[token] = []

        for token in sent:
            if token.dep_ == "nsubjpass" and token.head in objects.keys():
                objects[token.head].append(token)
                for token_1 in sent:
                    if token_1.dep_ == "compound" and token_1.head == token:
                        objects[token.head].append(token_1)
            if token.dep_ == "dobj" and token.head in objects.keys():
                objects[token.head].append(token)
                for token_1 in sent:
                    if token_1.dep_ == "compound" and token_1.head == token:
                        objects[token.head].append(token_1)

        for ent in sent.ents:
            if ent.label_ == "TIME" or ent.label_ == "DATE":
                if ent.root.head in durations.keys():
                    durations[ent.root.head].append(ent)
                elif ent.root.head.head in durations.keys():
                    durations[ent.root.head.head].append(ent)

        for token in sent:
            if token.dep_ == "advcl":
                for token_1 in sent:
                    if token_1.head == token and token_1.dep_ == "aux" and token_1.text == "to" and token.head in reasons.keys():
                        reasons[token.head].append(token_1.head)

        for token in sent:
            if token.dep_ == "pcomp" and token.head.head in reasons.keys():
                reasons[token.head.head].append(token)
    return root_verbs, objects, durations, reasons


print(extract_phrases(retain_verb, "I will cache your menstruation record ten years to know who you are "))

'''
for f in os.listdir("./data/privacy_pages"):
    policy = open("./data/privacy_pages/"+f, "r").read()
    print(extract_phrases(collect_verb, policy))
'''
