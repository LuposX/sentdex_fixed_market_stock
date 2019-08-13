import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

import sklearn
from sklearn import svm, preprocessing
from sklearn.metrics import classification_report, confusion_matrix
sns.set_style("darkgrid")

#-------------------------------------------------------------------------------------------------------
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
def randomizer():
    df = pd.DataFrame({"D1": range(5), "D2": range(5)}) 
    df2 = df.reindex(np.random.permutation(df.index))

#-------------------------------------------------------------------------------------------------------
def Build_Data_Set():
    
    # reads the csv to save it in ram
    data_df = pd.read_csv("Stock_market_full.csv")
    data_df.dropna(axis=0, inplace=True)
    
    # data_df = data_df[:100]
    
    # shuffles our data
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

    
    print("X std: ", X.std())
    
    return X, y

#-------------------------------------------------------------------------------------------------------
def Analyis(report=False):
    
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
X, y = Analyis(report=True) 
