import pandas as pd
import os
import time

import quandl

quandl.ApiConfig.api_key = "XXX"

path = "/datasets/intraQuarter"

def Stock_Prices():
    df = pd.DataFrame()
    statspath = path + "/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]
    
    for each_dir in stock_list[1:5]:
        try:
            ticker = each_dir.split("\\")[1]
            print(ticker)
            name = "WIKI/" + ticker.upper()
            data = quandl.get(name, trim_start="2000-12-12", trim_end="2018-12-12")
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis=1)
            
        except Exception as e1:
            print("E1: ", str(e1))
            time.sleep(2)
            try:
                ticker = each_dir.split("\\")[1]
                print(ticker)
                name = "WIKI/" + ticker.upper()
                data = quandl.get(name, trim_start="2000-12-12", trim_end="2018-12-12")
                data[ticker.upper()] = data["Adj. Close"]
                df = pd.concat([df, data[ticker.upper()]], axis=1)
                
            except Exception as e2:
                print("E2: ", str(e2))
    
    df.index.rename("Date", inplace=True)
    df.reset_index(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df.to_csv("stock_prices.csv", index=False)

    return df

df = Stock_Prices()
