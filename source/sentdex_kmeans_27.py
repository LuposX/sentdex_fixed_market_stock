# episode 27 Unsupervised Machine Learning - Flat Clustering with KMeans with Scikit-learn and Python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

sns.set_style("darkgrid")

# our data points
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

# our data points visulaized
sns.scatterplot(x, y)
plt.show()

# convert our datapoints in 1 "list"
X = np.array([[1, 2],
              [5, 8],
              [1.5, 1.8],
              [8, 8],
              [1, 0.6],
              [9, 11]])


# creating our cluster model
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids =  kmeans.cluster_centers_
labels =  kmeans.labels_

# communication is the key
print("centroids: ")
print(centroids)
print(" ")
print("labels: ")
print( labels)

# visulize our data
colors = ["green", "red",]
sns.scatterplot(x, y, hue=labels, palette=colors, s=90)
sns.scatterplot(centroids[:, 0], centroids[:, 1], marker="x", s=200, color="blue", linewidth=4)
plt.show()
