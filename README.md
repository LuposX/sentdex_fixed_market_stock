# sentdex_fixed_market_stock
Date of first upload: *09.08.2019*  
Date of last upload: *13.08.2019*    
This is a github repository for the youtube tutorial series from [sentdex](https://youtu.be/URTZ2jKCgBc). Stand: [Episode 18](https://www.youtube.com/watch?v=l68b0d92AHQ&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=18).   
This github repository is UNOFFICIAL
go here if you want to support sentdex:  
- [Sentdex YouTube](https://www.youtube.com/user/sentdex/)
- [Sentdex Website](https://pythonprogramming.net/)

Because the sentdex tutorial playlist is from 2014. Some libaries changed and the original code which sentdex uploaded on his [forum](https://pythonprogramming.net/) doesn't work anymore (at least for me). Therefore i want to offer my code that worked for me for those who 
it need.


# Use
1. Download the file for the corresponding episode in the **source** folder.
	
2. Most of the files need those datasets:   
-**YAHOO_INDEX_GSPC.csv** (can be found in the **dataset** folder)            
-**[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)** 
  
I also would recomend to either create the datasets you need, in the file you downloaded, with other python scripts from me (from the **source** folder) or to download the corresponding **datasets** from my folder. Do not use your own Datasets.  

3. Make sure to change, in the files you downloaded, the lines to the location of your **datasets** when needed. 

4. run the file with the command in the cmd:  
``` py sentdex_XXX_XXX.py ```  

**Notes:** 
In some files you need to change this line when you want to parse the whole dataset or less:  
``` for each_dir in stock_list[1:10]:```    
   
# License & Credits
MIT License means: https://choosealicense.com/licenses/mit/  
Credits sentdex: https://www.youtube.com/user/sentdex/
