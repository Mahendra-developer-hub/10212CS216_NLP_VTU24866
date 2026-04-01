import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence = "Will Jane go to the market"

words = word_tokenize(sentence)
tagged = pos_tag(words)

print(tagged)