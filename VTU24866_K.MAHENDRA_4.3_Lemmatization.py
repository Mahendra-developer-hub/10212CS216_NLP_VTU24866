import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("walking running plays studies")

for token in doc:
    print(token.text, "->", token.lemma_)