import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

from sklearn import svm
sns.set_style("darkgrid")

# just 2 random arrays as example for visualizen.
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

# creates a scatter plot with the datapoints from x and y.
sns.scatterplot(x, y)

X = np.array([[1, 2],
             [5, 8],
             [1.5, 1.8],
             [8, 8],
             [1, 0.6],
             [9, 11]])

# our y data in binar. Must be binar for using a classifier
Y = [0, 1, 0, 1, 0, 1]

# creating our classifier. Kernel="linear" means our border is a linear line. "C" is a variable you can play round with
clf = svm.SVC(kernel="linear", C=1.0)
# we "fit" our training data to our model. Also called we "train" our model
clf.fit(X, Y)

# we just predict some random numbers
pred = clf.predict([[10.58, 10.76]])
print("Prediction: ", pred) # output our prediction

# used for calculating how we plot our border from the classifier
w = clf.coef_[0]
a = -w[0] / w[1]

xx = np.linspace(0, 12) # geting x for ploting the line
yy = a * xx - clf.intercept_[0] / w[1]  # geting y for ploting the line

# we give our data different colors
custom_palette = ["red", "green"]

# we plot our data. "Hue" is our "third dimension" were we see how our classifier evaluated each sample
sns.scatterplot(x, y, hue=Y, palette=custom_palette) # that just plots the point
sns.lineplot(xx, yy, label="non weighted div") # that plots our border from the classiefier
plt.show() # we show our plot
