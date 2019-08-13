import pandas as pd
import numpy as np
import seaborn as sns

import sklearn
from sklearn import svm, preprocessing
from sklearn.metrics import classification_report
sns.set_style("darkgrid")

#-------------------------------------------------------------------------------------------------------
# our features
FEATURES =  ['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior month)']

#-------------------------------------------------------------------------------------------------------
# example from the video for a function that randomizes our data
def randomizer():
    df = pd.DataFrame({"D1": range(5), "D2": range(5)})
    df = df.reindex(np.random.permutation(df.index))

#-------------------------------------------------------------------------------------------------------
def Build_Data_Set():

    # reads the csv to save it in ram. Make sure to chaneg the path when you use it
    data_df = pd.read_csv("../datasets/Stock_market_full.csv")
    data_df.dropna(axis=0, inplace=True)

    # data_df = data_df[:100]

    # shuffles our data. You can use the sklearn dunction "shuffle" or the function from "sentdex"
    #data_df = data_df.reindex(np.random.permutation(data_df.index))
    data_df = sklearn.utils.shuffle(data_df)

    # converts our wished features to a 2d list
    X = np.array(data_df[FEATURES].values.tolist())

    # replaces our status thorught 0 or 1 | needs to be binar to use it
    y = (data_df["Status"]
        .replace("underperform", 0)
        .replace("outperform", 1)
        .values)

    # preprocessing your data | normalization
    X = preprocessing.scale(data_df[FEATURES])

    # prints the standart derivation should be close to 1 after normalization
    print("X std: ", X.std())

    return X, y

#-------------------------------------------------------------------------------------------------------
def Analyis(report=False):

    # size of our test data set. You can play around with that.
    test_size = 500

    # recall the Build_Data_Set() function to get X, y
    X, y = Build_Data_Set()
    print("len of x: ", len(X))
    print(" ")
    #print(X)

    # build our svm model
    clf = svm.SVC(kernel="linear", C=1.0)

    # trains our model
    clf.fit(X[:-test_size], y[:-test_size]) # [:-test_size] we are leaving the last 500 exampels out for testing later

    # predict our training exmaples
    pred = clf.predict(X[-test_size:])

    #prints classification report
    if report: print(classification_report(y[-test_size:], pred))

    return X, y

#-------------------------------------------------------------------------------------------------------
# calls our function and saves x and y (if you need them) you can turn on/off the report mode
X, y = Analyis(report=True) 
