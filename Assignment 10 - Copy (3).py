""" Assignment of 3rd march """

import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

features = df[["Study_Hours"]]
labels = df["Marks"]

print("\nFeatures:")
print(features)

print("\nLabels:")
print(labels)

prediction_hours = 9
predicted_marks = prediction_hours * 10

print("\nPredicted marks for", prediction_hours, "study hours:", predicted_marks)