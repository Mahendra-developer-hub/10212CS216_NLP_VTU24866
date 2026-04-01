import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

text = "NLTK is a powerful tool for NLP tasks. It's great!"
tokens = sent_tokenize(text)

print(tokens)