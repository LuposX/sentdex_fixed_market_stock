# for episode 22

import pandas as pd
import numpy as np

import os
import re

path = "/datasets/intraQuarter"

def Forward(gather=["Total Debt/Equity",
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

    file_list = os.listdir("episode21/html")

    for each_file in file_list[:]:

        ticker = each_file.split(".html")[0]
        full_file_path = "episode21/html/" + str(each_file)
        source = open(full_file_path, "r").read()

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

            # communication is the key
            print("Last processed file: ", str(ticker) + ".html")

            #----------------------------------------------------------------------------------------------------------------------------------------
            # only appending when there are no "N/A" values
            if value_list.count("N/A") > 20 | value_list.count(np.nan) > 20 | value_list.count() > 20 | value_list.isnull().count() > 20 | value_list.count(None) > 20 | value_list != None | value_list != []:
                pass
            else:
                df = df.append({'Date':np.nan,
                                    'Unix':np.nan,
                                    'Ticker':ticker,

                                    'Price':np.nan,
                                    'stock_p_change':np.nan,
                                    'SP500':np.nan,
                                    'sp500_p_change':np.nan,
                                    'Difference':np.nan,
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
                                     'Status':np.nan},
                                     ignore_index=True)



        except Exception as e6:
            print("e6: ", e6)
            break


    #----------------------------------------------------------------------------------------------------------------------------------------
    # saving the file with the right format
    def save(file_format):
        return  "forward_sample_WITH_NA." + file_format

    # df.to_excel(save("xlsx"), index=False)
    df.to_csv(save("csv"), index=False)

Forward()
