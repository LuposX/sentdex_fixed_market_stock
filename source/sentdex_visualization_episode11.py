import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

from sklearn import svm
sns.set_style("darkgrid")

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

sns.scatterplot(x, y)

X = np.array([[1, 2],
             [5, 8],
             [1.5, 1.8],
             [8, 8],
             [1, 0.6],
             [9, 11]])

Y = [0, 1, 0, 1, 0, 1]

clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, Y)

pred = clf.predict([[10.58, 10.76]])
print("Prediction: ", pred)

w = clf.coef_[0]
a = -w[0] / w[1]

xx = np.linspace(0, 12) # geting x for ploting the line
yy = a * xx - clf.intercept_[0] / w[1]  # geting y for ploting the line

custom_palette = ["red", "green"]

sns.scatterplot(x, y, hue=Y, palette=custom_palette)
sns.lineplot(xx, yy, label="non weighted div")
print(w)