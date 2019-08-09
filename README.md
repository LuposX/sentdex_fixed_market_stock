# sentdex_fixed_market_stock
Date of upload: 09.08.2019  
Fixed file from the youtube tutorial series from [sentdex](https://youtu.be/URTZ2jKCgBc) Stand: [Episode 12](https://www.youtube.com/watch?v=4WM6hB7l4Lc&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=12).

# Use
1. Download the file *sentdex_stock_market.py*.

2. Make sure you have the datasets:   
-[YAHOO_INDEX_GSPC.csv](https://github.com/michaelgu95/machine-learning-stocks/blob/master/YAHOO-INDEX_GSPC.csv)                
-[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)

3. Make sure to change the lines to the location of your datasets  
*path = "../intraQuarter" # insert here your path to the intraQuarter dataset*  
*sp500_df = pd.read_csv(".../datasets/YAHOO_INDEX_GSPC.csv") # insert here your path to the YAHOO_INDEX_GSPC.csv*  

4. run the file with the command in the cmd:  
``` py sentdex_stock_market.py ```  
it will create 2 files: *Stock_market.csv* and *Stock_market.xlsx* 

# Changes
**Bug Fixes:**
- Changed the line: *row = sp500_df\[(sp500_df.index == sp500_date)\]*  
  **to:** *row = sp500\[sp500\["Date"\] == sp500_date]*

- Changed the line: *sp500_value = float(row\["Adjusted Close"\])*  
  **to:** *sp500_value = float(row\["Adj Close"\])*  
  \(is necessary when you got your YAHOO_INDEX_GSPC.csv from here:   
  https://github.com/michaelgu95/machine-learning-stocks/blob/master/YAHOO-INDEX_GSPC.csv)
  
 - Changed the line: *'Shares Short (prior '*
  to: *'Shares Short (prior month)'*
 
  
**Features:**
- added df.to_excel() at the end to also save the file as xlsx format
- round sp500_value to 4 decimal points 
- added a extra ```try except```for better debuging
- changed unixtime from *float* to *int*

# License & Credits
MIT License means: https://choosealicense.com/licenses/mit/  
Credits sentdex: https://www.youtube.com/user/sentdex/
