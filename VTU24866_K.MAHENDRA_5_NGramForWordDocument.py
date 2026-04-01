import nltk
from nltk.util import ngrams
from collections import Counter

# Training corpus
corpus = [
    "The cat sat",
    "The cat ate fish",
    "The dog ate food"
]

# Tokenize words
tokens = []
for sentence in corpus:
    tokens.extend(sentence.lower().split())

print("Tokens:", tokens)

# -------------------------
# UNIGRAM
# -------------------------

unigrams = list(ngrams(tokens, 1))
unigram_counts = Counter(unigrams)

print("\nUnigrams:")
for word, count in unigram_counts.items():
    print(word, ":", count)

# -------------------------
# BIGRAM
# -------------------------

bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)

print("\nBigrams:")
for word, count in bigram_counts.items():
    print(word, ":", count)