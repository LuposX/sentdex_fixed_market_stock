[![License](https://img.shields.io/github/license/LuposX/sentdex_fixed_market_stock)](LICENSE) 
![Size](https://img.shields.io/github/repo-size/LuposX/sentdex_fixed_market_stock)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](hhttps://github.com/LuposX/sentdex_fixed_market_stock/issues/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7d14e2763577432b9afcbe1efffd4d52)](https://www.codacy.com/app/LuposX/sentdex_fixed_market_stock?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LuposX/sentdex_fixed_market_stock&amp;utm_campaign=Badge_Grade)

# About

Date of first upload: *09.08.2019*  
Date of last upload: *13.08.2019*
  
This is a github repository for the youtube tutorial series from [sentdex](https://youtu.be/URTZ2jKCgBc). Stand: [Episode 18](https://www.youtube.com/watch?v=l68b0d92AHQ&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=18).   
This github repository is UNOFFICIAL
go here if you want to support sentdex:  
-  [Sentdex YouTube](https://www.youtube.com/user/sentdex/)     
-  [Sentdex Website](https://pythonprogramming.net/)    

Because the sentdex tutorial playlist is from 2014. Some libaries changed and the original code which sentdex uploaded on his [forum](https://pythonprogramming.net/) doesn't work anymore (at least for me). Therefore i want to offer my code that worked for me for those who 
it need.   
If you have any Issued please open a **[Issue](https://github.com/LuposX/sentdex_fixed_market_stock/issues/new)** in github. 
   
## Use

1.  Download the file for the corresponding episode in the **source** folder.

2.  I would recomend to either create the datasets you need, in the file you downloaded, with other python scripts from me (from the **source** folder) or to download the corresponding **datasets** from my folder. DO NOT USE YOUR OWN DATASETS IT MIGHT NOT WORK.
More under [Datasets](#Datasets). 

3.  Make sure to change, in the files you downloaded, the lines to the location of your **datasets** when needed. 

4.  run the file with the command in the cmd:    
``` py sentdex_XXX_XXX.py ```      
   
**Notes:**     
-  In some files you need to change this line when you want to parse the whole dataset or less:      
``` for each_dir in stock_list[1:10]:```  

-  In addition to the libaries sentdex used in his playlist i use **Seaborn** can be downloaded [here](https://seaborn.pydata.org/installing.html).    
  
    
## Datasets  
Here i'll list the files and the datasets you need for them:   
  
**sentdex_visualization_episode11.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_visualization_episode11.py)**:**     
-  **None**      
  
**sentdex_stock_market_episode12.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_stock_market_episode12.py)**:**      
-  **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**    
-  **[Yahoo Index](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/YAHOO_INDEX_GSPC.csv)**   
  
**sentdex_visualization_episode13.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_visualization_episode13.py)**:**     
-  **None**    
  
**sentdex_prediction_episode15.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_prediction_episode15.py)**:**        
-  **[Stock_market_full.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_full.csv)**      
  
**sentdex_getData_episode17.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_getData_episode17.py)**:**      
-  **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**     
  
**sentdex_data_episode18.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_data_episode18.py)**:**    
-  **[Yahoo Index](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/YAHOO_INDEX_GSPC.csv)**     
-  **[Stock prices](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/stock_prices.zip)**    
  
  
## License & Credits
MIT License means: [Click me](https://choosealicense.com/licenses/mit/)   
Credits sentdex: [Click me](https://www.youtube.com/user/sentdex/)  

## Gitpod
If you dont want to download it because you dont know if it malicious or not or other reasons check the online ide out:  
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/LuposX/sentdex_fixed_market_stock/source)  
