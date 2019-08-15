import pandas as pd
import numpy as np
import statistics

import sklearn
from sklearn import svm, preprocessing
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

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


def Build_Data_Set():
    
    # reads the csv to save it in ram
    data_df = pd.read_csv("Stock_market_acc_WITH_NA.csv")
    # data_df.dropna(axis=0, inplace=True)
    
    # data_df = data_df[:100]
    
    # shuffles our data
    data_df = sklearn.utils.shuffle(data_df)
    
    # replaces the n/a in dataframe
    data_df = data_df.fillna(0)
    
    # converts our wished features to a 2d list
    X = np.array(data_df[FEATURES].values.tolist())
    
    # replaces our status thorught 0 or 1 | needs to be binar to use it 
    y = (data_df["Status"]
        .replace("underperform", 0)
        .replace("outperform", 1)
        .values)
    
    # preprocessing your data | normalization
    X = preprocessing.scale(data_df[FEATURES])
    
    z = np.array(data_df[["stock_p_change", "sp500_p_change"]])
    
    print("X std: ", X.std())
    
    return X, y, z


def Analyis(report=False):
    
    # how big our test size is (number of examples)
    test_size = 1000
    
    # how much we invest in the stocks
    invest_amount = 10000
    total_invest = 0
    if_market = 0
    if_strat = 0
    
    # call the Build_Data_Set() function to get X, y
    X, y, z = Build_Data_Set()
    print("len of x: ", len(X))
    print(" ")
    #print(X)
    
    # build our svm model
    clf = svm.SVC(kernel="linear", C=1.0)
    
    # trains our model
    clf.fit(X[:-test_size], y[:-test_size]) # [:-test_size] we are leaving the last 500 exampels out for testing later

    # calculating the performance of our model | How much profit we would make
    for x in range(1, test_size+1):
        if clf.predict([X[-x]])[0] == 1:
            invest_return = invest_amount + (invest_amount * (z[-x][0] / 100.0))
            market_return = invest_amount + (invest_amount * (z[-x][1] / 100.0))
            total_invest += 1
            if_market += market_return
            if_strat += invest_return
                                             
    # predict our training exmaples
    pred = clf.predict(X[-test_size:])
    
    #prints classification report
    if report: print(classification_report(y[-test_size:], pred))
    if report: print("Model accuracy: ", accuracy_score(y[-test_size:], pred))
    if report: print(" ")
    
    # prints How much profit we would make  
    print("Total Trades: ", total_invest)

    print("Ending with strategy: ", if_strat)
    print("Ending with Market: ", if_market)
                                             
    compared = round(((if_strat - if_market) / if_market * 100.0), 3)
    do_nothing = total_invest * invest_amount
    
    avg_market = round(((if_market - do_nothing) / do_nothing) * 100.0, 3)
    avg_strat = round(((if_strat - do_nothing) / do_nothing) * 100.0, 3)
    
    print("Compared to market, we earn: ", str(compared) + "% more")
    print("Average investment return: ", str(avg_strat) + "%")
    print("Average market return: ", str(avg_market) + "%")    
    # print("Average investment return: ", )                                      

Analyis(report=True) 
