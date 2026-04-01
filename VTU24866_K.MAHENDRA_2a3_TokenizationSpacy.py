import spacy

nlp = spacy.load("en_core_web_sm")

text = "spaCy is an efficient library for production-ready NLP. It's fast!"

doc = nlp(text)

tokens = [token.text for token in doc]

print("Word Tokens:", tokens)