import spacy

nlp = spacy.load("en_core_web_sm")

text = "spaCy is an efficient library for production-ready NLP. It's fast!"

doc = nlp(text)

sentences = [sent.text for sent in doc.sents]

print("Sentence Tokens:", sentences)