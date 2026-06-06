""" Sentiment Vectorization (BoW & TF-IDF) """
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

dataset = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]

bow = CountVectorizer()
bow_matrix = bow.fit_transform(dataset)

print("Bag of Words Matrix:")
print(pd.DataFrame(bow_matrix.toarray(), columns=bow.get_feature_names_out()))
print()

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(dataset)

print("TF-IDF Matrix:")
print(pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out()))