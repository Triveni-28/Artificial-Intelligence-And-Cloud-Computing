import random
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    word_scores = list(zip(feature_names, scores))
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)
    return [word for word, score in sorted_words[:top_n]]

def chatbot():
    print("Smart NLP Chatbot (type 'bye' to exit)")
    user_name = None
    greetings = ["hello", "hi", "hey"]
    greeting_responses = ["Hello!", "Hi there!", "Hey! How can I help you?"]

    while True:
        user_input = input("\nYou: ").lower()

        if "bye" in user_input:
            print("Bot: Goodbye! 👋")
            break

        elif any(word in user_input for word in greetings):
            print("Bot:", random.choice(greeting_responses))

        elif "my name is" in user_input:
            user_name = user_input.replace("my name is", "").strip()
            print(f"Bot: Nice to meet you, {user_name}!")

        elif "what is my name" in user_input:
            if user_name:
                print(f"Bot: Your name is {user_name}.")
            else:
                print("Bot: I don't know your name yet.")

        elif "ai" in user_input:
            print("Bot: AI means Artificial Intelligence.")

        elif "llm" in user_input:
            print("Bot: LLM stands for Large Language Model.")

        elif "keywords" in user_input or "extract" in user_input:
            text = input("Bot: Enter text to extract keywords:\nYou: ")
            keywords = extract_keywords(text)
            print("Bot: Top Keywords:", keywords)

        elif any(word in user_input for word in ["death", "kill", "suicide"]):
            print("Bot: That sounds serious. If you want to talk, I'm here to listen.")

        else:
            responses = [
                "I'm not sure I understand, can you rephrase?",
                "Interesting, tell me more!",
                "Can you explain that differently?"
            ]
            print("Bot:", random.choice(responses))

chatbot()