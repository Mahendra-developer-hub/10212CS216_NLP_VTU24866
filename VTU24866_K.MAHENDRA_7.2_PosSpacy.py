import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Will Jane go to the market")

for token in doc:
    print(token.text, token.pos_)