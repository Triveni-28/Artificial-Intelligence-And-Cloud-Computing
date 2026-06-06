"""Threshold Experiment (Cancer Dataset)"""
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

probs = model.predict_proba(X_test)[:, 1]

thresholds = [0.3, 0.5, 0.7]

results = []

for t in thresholds:
    y_pred = (probs >= t).astype(int)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    
    results.append([t, acc, prec, rec])

df = pd.DataFrame(results, columns=["Threshold", "Accuracy", "Precision", "Recall"])
print(df)