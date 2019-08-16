# for episode 24

import pandas as pd
import numpy as np

import os
import time
from datetime import datetime

import re

path = "../datasets/intraQuarter"
sp500_df = pd.read_csv("../datasets/YAHOO_INDEX_GSPC.csv")
stock_df = pd.read_csv("../datasets/stock_prices.csv")

def Key_Stats(return_true_or_false=False, gather=["Total Debt/Equity",
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
                                                    'Shares Short (prior ']):

    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference',
                                 ##############
                                 'DE Ratio',
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
                                 'Shares Short (prior month)',
                                 ##############
                                 'Status'])

    ticker_list = []

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        ticker_list.append(ticker)

        # starting_stock_value = False
        # starting_sp500_value = False


        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                #date_stamp = pd.to_datetime(date_stamp, format='%Y%m%d') # added new
                unix_time = int(time.mktime(date_stamp.timetuple()))
                full_file_path = each_dir+'/'+file
                source = open(full_file_path,'r').read()
                try:
                    value_list = []

                    for each_data in gather:
                        try:
                            regex = re.escape(each_data) + r'.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?</td>'
                            value = re.search(regex, source)
                            value = (value.group(1))


                            if "B" in value:
                                value = float(value.replace("B",''))*1000000000

                            elif "M" in value:
                                value = float(value.replace("M",''))*1000000

                            value_list.append(value)

                        except:
                            value = np.nan
                            value_list.append(value)


                    #------------------------------------------------------------------------------------------------------------------------------------
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime("%Y-%m-%d")
                        row = sp500_df[(sp500_df["Date"] == sp500_date)]
                        sp500_value = float(row["Adj Close"])
                        sp500_value = round(sp500_value, 4)  

                    except:
                        try:
                            sp500_date = datetime.fromtimestamp(unix_time - 259200).strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df["Date"] == sp500_date)]
                            sp500_value = float(row["Adj Close"])
                            sp500_value = round(sp500_value, 4) 

                        except Exception as e2:
                             # print(str(e),'a;lsdkfh',file,ticker)
                             print("sp500: ", e2)
                             sp500_value = np.nan

                    #------------------------------------------------------------------------------------------------------------------------------------
                    one_year_later = int(unix_time + 31536000)

                    #------------------------------------------------------------------------------------------------------------------------------------
                    try:
                        sp500_1y = datetime.fromtimestamp(one_year_later).strftime("%Y-%m-%d")
                        row = sp500_df[(sp500_df["Date"] == sp500_1y)]
                        sp500_1y_value = float(row["Adj Close"])
                        sp500_value = round(sp500_value, 4) 

                    except:
                        try:
                            sp500_1y = datetime.fromtimestamp(one_year_later - 259200).strftime("%Y-%m-%d")
                            row = sp500_df[(sp500_df["Date"] == sp500_1y)]
                            sp500_1y_value = float(row["Adj Close"])
                            sp500_value = round(sp500_value, 4)  

                        except Exception as e3:
                            print("sp500 1y later: ", e3)
                            sp500_value = np.nan

                    #------------------------------------------------------------------------------------------------------------------------------------
                    try:
                        stock_price_1y = datetime.fromtimestamp(one_year_later).strftime('%Y-%m-%d')
                        row = stock_df[(stock_df["Date"] == stock_price_1y)][ticker.upper()]
                        stock_1y_value = round(float(row),2)

                    except:
                        try:
                            stock_price_1y = datetime.fromtimestamp(one_year_later - 259200).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df["Date"] == stock_price_1y)][ticker.upper()]
                            stock_1y_value = round(float(row), 2)

                        except Exception as e4:
                            print("stock price 1y later: ", str(e4))
                            # print(" ")
                            stock_1y_value = np.nan


                    #------------------------------------------------------------------------------------------------------------------------------------
                    try:
                        stock_price = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = stock_df[(stock_df["Date"] == stock_price)][ticker.upper()]
                        stock_price = round(float(row), 2)    

                    except:
                        try:
                            stock_price = datetime.fromtimestamp(unix_time - 259200).strftime('%Y-%m-%d')
                            # ----------------------------------------------------------------------------------------
                            row = stock_df[(stock_df["Date"] == stock_price)][ticker.upper()] # this line fails
                            # ----------------------------------------------------------------------------------------

                            stock_price = round(float(row), 2) 
                            # print(stock_price)

                        except Exception as e5:
                            stock_price = np.nan
                            print("stock price: ", str(e5))

                    #---------------------------------------------------------------------------------------------------------------------------------
                    try:
                        stock_p_change = round((((stock_1y_value - stock_price) / stock_price) * 100), 2)
                        sp500_p_change = round((((sp500_1y_value - sp500_value) / sp500_value) * 100), 2)
                    except:
                        stock_p_change = np.nan
                        sp500_p_change = np.nan

                    try:
                        difference = stock_p_change - sp500_p_change
                    except:
                        difference = np.nan

                    if difference > 5: # when its better than 5 %
                        status = 1
                    else:
                        status = 0

                    #----------------------------------------------------------------------------------------------------------------------------------------
                    # only appending when there are no "N/A" values
                    if value_list.count("N/A") > 20 | value_list.count(np.nan) > 20 | value_list.count() > 20 | value_list.isnull().count() > 20:
                        pass
                    else:
                        print("We're are in the directory: ", str(ticker))
                        df = df.append({'Date':date_stamp,
                                            'Unix':unix_time,
                                            'Ticker':ticker,

                                            'Price':stock_price,
                                            'stock_p_change':stock_p_change,
                                            'SP500':sp500_value,
                                            'sp500_p_change':sp500_p_change,
                                            'Difference':difference,
                                            'DE Ratio':value_list[0],
                                            #'Market Cap':value_list[1],
                                            'Trailing P/E':value_list[1],
                                            'Price/Sales':value_list[2],
                                            'Price/Book':value_list[3],
                                            'Profit Margin':value_list[4],
                                            'Operating Margin':value_list[5],
                                            'Return on Assets':value_list[6],
                                            'Return on Equity':value_list[7],
                                            'Revenue Per Share':value_list[8],
                                            'Market Cap':value_list[9],
                                             'Enterprise Value':value_list[10],
                                             'Forward P/E':value_list[11],
                                             'PEG Ratio':value_list[12],
                                             'Enterprise Value/Revenue':value_list[13],
                                             'Enterprise Value/EBITDA':value_list[14],
                                             'Revenue':value_list[15],
                                             'Gross Profit':value_list[16],
                                             'EBITDA':value_list[17],
                                             'Net Income Avl to Common ':value_list[18],
                                             'Diluted EPS':value_list[19],
                                             'Earnings Growth':value_list[20],
                                             'Revenue Growth':value_list[21],
                                             'Total Cash':value_list[22],
                                             'Total Cash Per Share':value_list[23],
                                             'Total Debt':value_list[24],
                                             'Current Ratio':value_list[25],
                                             'Book Value Per Share':value_list[26],
                                             'Cash Flow':value_list[27],
                                             'Beta':value_list[28],
                                             'Held by Insiders':value_list[29],
                                             'Held by Institutions':value_list[30],
                                             'Shares Short (as of':value_list[31],
                                             'Short Ratio':value_list[32],
                                             'Short % of Float':value_list[33],
                                             'Shares Short (prior month)':value_list[34],
                                             'Status':status},
                                             ignore_index=True)



                except Exception as e6:
                    print("e6: ", e6)
                    break


    #----------------------------------------------------------------------------------------------------------------------------------------
    # saving the file with the right format
    def save(file_format):
        return  "Stock_market_acc_WITH_NA_enhanced." + file_format

    # df.to_excel(save("xlsx"), index=False)
    df.to_csv(save("csv"), index=False)

    if return_true_or_false:
        return df, ticker_list

    df, ticker_list = Key_Stats(return_true_or_false=True)
