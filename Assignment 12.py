""" Assignment of 9th march """

from sklearn.linear_model import LinearRegression
import numpy as np

sizes = np.array([500, 700, 900, 1100, 1300]).reshape(-1,1)
prices = np.array([100000, 150000, 180000, 220000, 260000])

model = LinearRegression()
model.fit(sizes, prices)

new_size = np.array([[1000]])
predicted_price = model.predict(new_size)

print("Predicted price for 1000 sq ft house:", predicted_price[0])