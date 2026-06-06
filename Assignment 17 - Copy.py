""" Assignment (19/03/2026) """
# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 2: Create dataset
data = {
    'Age': [45, 50, 30, 35, 60, 40],
    'Cholesterol': [230, 250, 180, 190, 270, 200],
    'BP': [130, 140, 120, 125, 150, 135],
    'HeartRate': [150, 140, 170, 165, 130, 160],
    'Target': [1, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

# Step 3: Features & labels
X = df[['Age', 'Cholesterol', 'BP', 'HeartRate']]
y = df['Target']

# Step 4: Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Step 6: Model training
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 7: Prediction
y_pred = model.predict(X_test)

# Step 8: Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 9: New patient prediction
new_patient = scaler.transform([[48, 240, 138, 145]])
prediction = model.predict(new_patient)

if prediction[0] == 1:
    print("High Risk of Heart Disease")
else:
    print("Low Risk of Heart Disease")