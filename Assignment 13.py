""" Assignment of 10th march """ 

spam_words = ["win", "free", "offer", "prize", "money"]

email = input("Enter email message: ").lower()

spam_score = 0

for word in spam_words:
    if word in email:
        spam_score += 1

if spam_score >= 2:
    print("This email is likely SPAM")
else:
    print("This email looks SAFE")