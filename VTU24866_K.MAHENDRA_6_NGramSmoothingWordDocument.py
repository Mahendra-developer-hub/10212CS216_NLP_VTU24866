from collections import Counter
from nltk.util import ngrams

# Corpus
corpus = "I am a human"

# Tokenization
tokens = corpus.lower().split()

# -------------------------
# BIGRAM COUNTS
# -------------------------

bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)

print("Bigram Counts:")
print(bigram_counts)

# -------------------------
# UNIGRAM COUNTS
# -------------------------

unigram_counts = Counter(tokens)

print("\nUnigram Counts:")
print(unigram_counts)

# Vocabulary size
V = len(set(tokens))

# -------------------------
# LAPLACE SMOOTHING
# -------------------------

print("\nLaplace Smoothing Probabilities:")

for bigram in bigram_counts:
    w1, w2 = bigram
    
    count_bigram = bigram_counts[bigram]
    count_unigram = unigram_counts[w1]
    
    probability = (count_bigram + 1) / (count_unigram + V)
    
    print(f"P({w2}|{w1}) = {probability:.3f}")

# -------------------------
# INTERPOLATION
# -------------------------

print("\nInterpolation Probability Example:")

lambda1 = 0.7
lambda2 = 0.3

# Example bigram probability
bigram_prob = 0.5
unigram_prob = 0.25

interpolated_prob = lambda1 * bigram_prob + lambda2 * unigram_prob

print("Interpolated Probability =", interpolated_prob)