"""Data Cleaning & Preprocessing """ 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'age': [25, 30, None, 35, 30, None],
    'salary': [50000, None, 60000, 70000, None, 50000],
    'city': ['hyderabad', 'HYDERABAD', 'Hyderabad', 'chennai', 'CHENNAI', 'hyderabad'],
    'experience': [2, 3, 5, 7, 3, 2]
}

df = pd.DataFrame(data)

df = df.drop_duplicates()

df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].mean())

df['city'] = df['city'].str.lower()

scaler = MinMaxScaler()
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

print(df)