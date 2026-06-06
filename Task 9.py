""" 27th FEB"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

k_values = range(1, 16)
accuracy_euclidean = []
accuracy_manhattan = []

for k in k_values:
    model_eu = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    model_eu.fit(X_train, y_train)
    pred_eu = model_eu.predict(X_test)
    accuracy_euclidean.append(accuracy_score(y_test, pred_eu))

    model_man = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
    model_man.fit(X_train, y_train)
    pred_man = model_man.predict(X_test)
    accuracy_manhattan.append(accuracy_score(y_test, pred_man))

plt.plot(k_values, accuracy_euclidean, label='Euclidean')
plt.plot(k_values, accuracy_manhattan, label='Manhattan')
plt.xlabel("K value")
plt.ylabel("Accuracy")
plt.title("Accuracy vs K")
plt.legend()
plt.show()