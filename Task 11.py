""" Loan Approval Prediction """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    'income': [25000, 40000, 50000, 60000, 70000, 80000],
    'credit_score': [600, 650, 700, 720, 750, 780],
    'loan_amount': [10000, 15000, 20000, 25000, 30000, 35000],
    'employment_years': [1, 2, 3, 4, 5, 6],
    'loan_approved': [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['income', 'credit_score', 'loan_amount', 'employment_years']]
y = df['loan_approved']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = [[55000, 710, 22000, 3]]
prediction = model.predict(new_data)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")