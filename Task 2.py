"""Customer Segmentation (K-Means)"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'Age': [19, 21, 20, 23, 31, 35, 40, 60],
    'Annual_Income': [15, 16, 17, 18, 40, 42, 45, 60],
    'Spending_Score': [39, 40, 41, 42, 60, 65, 70, 80]
}

df = pd.DataFrame(data)

X = df[['Annual_Income', 'Spending_Score']]

kmeans = KMeans(n_clusters=2)
df['Cluster'] = kmeans.fit_predict(X)

print("Centroids:\n", kmeans.cluster_centers_)

plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'], cmap='viridis')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Mall Customer Segmentation")
plt.legend()
plt.show()