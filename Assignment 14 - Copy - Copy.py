""" Assignment of 11th march """ 

import numpy as np
from sklearn.cluster import KMeans

data = np.array([
    [20, 15],
    [22, 16],
    [25, 18],
    [40, 60],
    [42, 65],
    [45, 62],
    [60, 20],
    [62, 22],
    [65, 25]
])

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

labels = kmeans.labels_

print("Customer Groups:")
for i in range(len(data)):
    print("Customer", i+1, "-> Group", labels[i])