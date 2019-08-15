import urllib.request
import os
import time

path = "/datasets/intraQuarter"

def Check_Yahoo():
    statspath = path + "/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    # Added a counter to call out how many files we've already added
    counter = 0
    for e in stock_list[1:]:
        try:
            e = e.replace("/datasets/intraQuarter/_KeyStats\\", "")

            # for html | sentdex way
            link1 = "https://finance.yahoo.com/quote/"+e.upper()+"/key-statistics?p="+e.upper()
            resp1 = urllib.request.urlopen(link1).read()
            save1 = "episode21/html/"+str(e)+".html"
            store1 = open(save1, "w")
            store1.write(str(resp1))
            store1.close()

            # for json | tomgs way: https://github.com/tomgs/sentdexworkarounds
            link2 = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+e.upper()+"?modules=assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,cashflowStatementHistory,balanceSheetHistory"
            resp2 = urllib.request.urlopen(link2).read()
            save2 = "episode21/json/"+str(e)+".json"
            store2 = open(save2, "w")
            store2.write(str(resp2))
            store2.close()

            #Print some stuff
            counter +=1
            print("We processed: " + str(counter) + " Files.")
            print("We're are in the directory: ", str(e))

        except Exception as e:
            print(str(e))
            time.sleep(2)

Check_Yahoo()
