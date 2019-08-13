# sentdex_fixed_market_stock
Date of upload: 09.08.2019  
This is a github repository for the youtube tutorial series from [sentdex](https://youtu.be/URTZ2jKCgBc). Stand: [Episode 18](https://www.youtube.com/watch?v=l68b0d92AHQ&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=18). This is a github repository is UNOFFICIAL
go here if you want to support sentdex:  
- [Sentdex YouTube](https://www.youtube.com/user/sentdex/)
- [Sentdex Website](https://pythonprogramming.net/)

Because the sentdex tutorial playlist is from 2014. Some libaries changed and the original code which sentdex uploaded on his [forum](https://pythonprogramming.net/) doesn't work anymore (at least for me). Therefore i want to offer my code that worked for me for those who 
it need.


# Use
1. Download the file *sentdex_stock_market_episode12.py*.

2. Make sure you have the datasets:   
-[YAHOO_INDEX_GSPC.csv](https://github.com/michaelgu95/machine-learning-stocks/blob/master/YAHOO-INDEX_GSPC.csv)                
-[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)

3. Make sure to change the lines to the location of your datasets  
*path = "../intraQuarter" # insert here your path to the intraQuarter dataset*  
*sp500_df = pd.read_csv(".../datasets/YAHOO_INDEX_GSPC.csv") # insert here your path to the YAHOO_INDEX_GSPC.csv*  

4. run the file with the command in the cmd:  
``` py sentdex_stock_market.py ```  
it will create 2 files: *Stock_market.csv* and *Stock_market.xlsx*  

**Notes:**   
When you want to parse the whole data.   
Make sure to change this line from:  
``` for each_dir in stock_list[1:10]:```  
**to:**  
``` for each_dir in stock_list[1:]:```    
  
I also would recommend to delete this line:    
```
if value_list.count("N/A") > 0:    
    pass 
``` 


**Image without N/A values:**  
![Without N/A values](/images/image_without_na_values.png)

**Image with N/A values:**  
![Without N/A values](/images/image_with_na_values.png)
           

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
