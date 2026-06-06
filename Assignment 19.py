""" Assignment (21/03/2026) """
import nltk
nltk.download('stopwords')

import string
from nltk.corpus import stopwords

text = "This is a SAMPLE text!! With punctuation & STOPWORDS."

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Remove stopwords
stop_words = set(stopwords.words('english'))
words = text.split()
cleaned = [w for w in words if w not in stop_words]

print("Cleaned Text:", " ".join(cleaned))