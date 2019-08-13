import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

from sklearn import svm, preprocessing
sns.set_style("darkgrid")

 #--------------------------------------------------------------------------------------------------------------------------
def Build_Data_Set(features=["DE Ratio", 
                             "Trailing P/E"]):
    
    # reads the csv to save it in ram
    data_df = pd.read_csv("Stock_market_full.csv")
    data_df.dropna(axis=0, inplace=True)
    
    # uncomment this if you want to use less data
    # data_df = data_df[:100]
    
    # converts our wished features to a 2d list
    X = np.array(data_df[features].values)
    
    # replaces our status thorught 0 or 1 | needs to be binar to use it 
    y= (data_df["Status"]
        .replace("underperform", 0)
        .replace("outperform", 1)
        .values)
    
    # normalization our data 
    X = preprocessing.scale(X)
    
    return X, y

 #--------------------------------------------------------------------------------------------------------------------------
def Analyis():
    # recall the Build_Data_Set() function to get X, y
    X, y = Build_Data_Set()
    
    # build our svm model
    clf = svm.SVC(kernel="linear", C=1.0)
    
    # trains our model
    clf.fit(X, y)
    
    # variables to visualize our model
    w = clf.coef_[0]
    a = -w[0] / w[1]
    
    xx = np.linspace(min(X[:, 0]), max(X[:, 0])) # "X[:, 0]" the 0 stands for the axis first axis 
    yy = a * xx - clf.intercept_[0] / w[1]
      
    return xx, yy, X, y

#--------------------------------------------------------------------------------------------------------------------------
# calls our function
xx, yy, X, y = Analyis()
#--------------------------------------------------------------------------------------------------------------------------
# plot figure size from in inches
plt.figure(figsize=(9, 6))

sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y) # plots the data points
sns.lineplot(x=xx, y=yy) # plots the border from the classifier

plt.xlabel("De Ratio") # name our x-axis 
plt.ylabel("Tailin P/E") # name our y-axis
plt.title("Underperformer/Outperformer from stock companies", fontsize=16) # give our plot a title
plt.legend(labels=["non weighted line", "0: underperform", "1: outperform"]) # adds a legend
plt.show() # shows our plot
