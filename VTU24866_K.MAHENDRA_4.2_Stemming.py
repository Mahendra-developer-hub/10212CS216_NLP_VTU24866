from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["walking", "studies", "worked"]

for w in words:
    print(w, "->", ps.stem(w))