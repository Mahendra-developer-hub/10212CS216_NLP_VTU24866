from transformers import AutoTokenizer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Sample text
text = "This is a sample sentence with some stopwords"

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords before tokenization
filtered_tokens = [
    token for token in tokenizer.tokenize(text)
    if token.lower() not in stop_words
]

print(filtered_tokens)