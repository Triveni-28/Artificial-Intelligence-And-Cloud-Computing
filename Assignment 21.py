""" Assignment (26/03/2026) """
reviews = [
    "The movie was amazing and fantastic!",
    "I loved the acting and story.",
    "The movie was okay, not great.",
    "I did not like the film.",
    "Worst movie ever."
]

positive_words = ["amazing", "fantastic", "loved", "great"]
negative_words = ["worst", "not", "bad", "hate"]

for review in reviews:
    score = 0
    for word in positive_words:
        if word in review.lower():
            score += 1
    for word in negative_words:
        if word in review.lower():
            score -= 1

    if score > 0:
        print(review, "→ Positive")
    elif score < 0:
        print(review, "→ Negative")
    else:
        print(review, "→ Neutral")