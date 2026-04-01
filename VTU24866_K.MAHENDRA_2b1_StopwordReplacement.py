from transformers import BertTokenizer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Sample text
text = "This is a sample sentence with some stopwords"

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Replace stopwords with [STOP]
processed_text = ' '.join([
    word if word.lower() not in stop_words else '[STOP]'
    for word in text.split()
])

# Tokenize processed text
tokens = tokenizer.tokenize(processed_text)

print(tokens)