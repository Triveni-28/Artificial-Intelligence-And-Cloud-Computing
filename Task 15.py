from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

reviews = [
    "The movie was amazing",
    "I loved the movie",
    "Fantastic and wonderful film",
    "Great acting and story",
    "Excellent movie",

    "The movie was terrible",
    "I hated the movie",
    "Worst film ever",
    "Very boring movie",
    "Bad acting and story",

    "The movie was okay",
    "It was average",
    "Nothing special",
    "It was fine",
    "Just normal movie"
]

labels = [
    "positive","positive","positive","positive","positive",
    "negative","negative","negative","negative","negative",
    "neutral","neutral","neutral","neutral","neutral"
]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(reviews)

model = LogisticRegression()
model.fit(X, labels)
user_input = input("Enter a movie review: ")
user_vector = vectorizer.transform([user_input])
prediction = model.predict(user_vector)
print("Sentiment:", prediction[0])