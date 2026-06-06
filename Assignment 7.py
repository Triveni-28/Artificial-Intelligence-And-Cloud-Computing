""" Assignment of 24th Feb """

import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Neha", "Kiran", "Divya"],
    "Math": [85, 92, 78, 88, None],
    "Science": [90, 85, 80, None, 95],
    "English": [88, 91, 76, 84, 89]
}

df = pd.DataFrame(data)

print("Top rows of dataset:")
print(df.head())

print("\nHighest value in each column:")
print(df.max(numeric_only=True))

print("\nMissing values in each column:")
print(df.isnull().sum())