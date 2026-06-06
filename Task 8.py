"""18th FEB """
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [200, 220, 250, 270, 300, 320],
    'Marketing_Spend': [50, 60, 55, 65, 70, 75],
    'Profit': [150, 160, 195, 205, 230, 245]
}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Revenue'])
plt.title("Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

plt.scatter(df['Marketing_Spend'], df['Profit'])
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.title("Marketing vs Profit")
plt.show()

correlation = df[['Revenue', 'Marketing_Spend', 'Profit']].corr()
print("Correlation Matrix:\n", correlation)