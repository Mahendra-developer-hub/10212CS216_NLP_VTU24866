# Sample corpus
sentence = "the quick brown fox jumps over the lazy dog"

# Convert sentence to words
words = sentence.split()

# Build Bigram Model
bigram_model = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in bigram_model:
        bigram_model[word] = []

    bigram_model[word].append(next_word)

# Last word
bigram_model[words[-1]] = ["END"]

print("Bigram Model:")
print(bigram_model)

# Word Generation
current_word = "the"
generated_sentence = [current_word]

while current_word != "END":
    next_words = bigram_model.get(current_word)

    if next_words:
        next_word = next_words[0]   # choose first word
        if next_word != "END":
            generated_sentence.append(next_word)
        current_word = next_word
    else:
        break

print("\nGenerated Sentence:")
print(" ".join(generated_sentence))