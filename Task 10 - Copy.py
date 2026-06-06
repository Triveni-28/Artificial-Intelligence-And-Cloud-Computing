""" Task - 13th March """
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

text = input("Enter text: ")

text = text.lower()

text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()

stop_words = set(stopwords.words('english'))
cleaned_words = [word for word in words if word not in stop_words]

cleaned_text = " ".join(cleaned_words)

print("Cleaned Text:", cleaned_text)