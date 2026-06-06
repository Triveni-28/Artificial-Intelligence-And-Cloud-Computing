"""Assignment (18/03/2026) """
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Annual_Income': [15, 16, 17, 50, 55, 60, 80, 85],
    'Spending_Score': [39, 40, 41, 60, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

# K-Means model
kmeans = KMeans(n_clusters=2)
df['Cluster'] = kmeans.fit_predict(df)

# Plot
plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()