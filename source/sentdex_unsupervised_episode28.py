# episode 28 unsupervised Machine Learning - Hierarchical Clustering with Mean Shift Scikit-learn and Python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs  # to generate random data samples

sns.set_style("darkgrid")

# Around those center we create our samples
centers = [[1, 1], [5, 5], [3, 10]]

# "y" are the real labels
X, y = make_blobs(n_samples = 200, centers = centers, cluster_std = 1)

# plotting our data with seaborn
sns.scatterplot(X[:,0], X[:,1])
plt.show()

# training our model
ms = MeanShift()
ms.fit(X)

# dont confuse those labels with "y". labels are the "predicted" labels. y are the real labels
labels = ms.labels_
cluster_centers = ms.cluster_centers_  # estimated centers of our data sets

# estimated number of cluster
n_clusters = len(np.unique(labels))

# Communication is the key
print("Number of estimated cluster: ", n_clusters)
# print("Labels: ", labels)
print("Cluster Centeres: ")
print(np.round(cluster_centers, 2))

plt.figure(figsize=(8,7))
sns.scatterplot(X[:, 0], X[:, 1], hue=labels, palette="summer", legend="full")
sns.scatterplot(cluster_centers[:, 0], cluster_centers [:, 1], marker="x", s=200, color="magenta", linewidth=4)
plt.show()