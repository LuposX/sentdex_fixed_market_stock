[![License](https://img.shields.io/github/license/LuposX/sentdex_fixed_market_stock)](LICENSE) 
![Size](https://img.shields.io/github/repo-size/LuposX/sentdex_fixed_market_stock)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7d14e2763577432b9afcbe1efffd4d52)](https://www.codacy.com/app/LuposX/sentdex_fixed_market_stock?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LuposX/sentdex_fixed_market_stock&amp;utm_campaign=Badge_Grade)

# About

Date of first upload: *09.08.2019*  
Date of last update: *18.08.2019*
  
This is a github repository for the youtube tutorial series from [sentdex](https://youtu.be/URTZ2jKCgBc). Stand: Episode 28/ Episode 28.   
This github repository is UNOFFICIAL
go here if you want to support sentdex:  
-   [Sentdex YouTube](https://www.youtube.com/user/sentdex/)     
-   [Sentdex Website](https://pythonprogramming.net/)    

Because the sentdex tutorial playlist is from 2014. Some libaries changed and the original code which sentdex uploaded on his [forum](https://pythonprogramming.net/) doesn't work anymore (at least for me). Therefore i want to offer my code that worked for me for those who 
it need. You can also find the datasets in the **dataset** folder if you miss some datasets.  
If you have any Issued please open a **[Issue](https://github.com/LuposX/sentdex_fixed_market_stock/issues/new)** in github. 
   
## Use

1.  Download the file for the corresponding episode in the **source** folder.

2. Make sure you have all libaries you need to run the file. I listed the libaries you need in **requirements.txt**

3.  I would recomend to either create the datasets you need, in the file you downloaded, with other python scripts from me (from the **source** folder) or to download the corresponding **datasets** from my folder. DO NOT USE YOUR OWN DATASETS IT MIGHT NOT WORK.
More under [Prerequisite](#Prerequisite). 

4.  Make sure to change, in the files you downloaded, the lines to the location of your **datasets** when needed. 

5.  run the file with the command in the cmd:    
``` py sentdex_XXX_XXX.py ```      
   
**Notes:**     
-   In some files you need to change this line when you want to parse the whole dataset or less:      
``` for each_dir in stock_list[1:10]:```  

-   In addition to the libaries sentdex used in his playlist i use **Seaborn** can be downloaded [here](https://seaborn.pydata.org/installing.html).    
  
    
## Prerequisites 

Here i'll list the prerequisites you need for each file. You can find them in the dataset folder on this repo or when you click on corresponding link.
	  
<details>
  <summary>Click to expand and to see the necessary prerequisite for each file.</summary>  
    
**sentdex_visualization_episode11.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_visualization_episode11.py) it needs:  
-   **[matplotlib](https://matplotlib.org/)**  
-   **[seaborn](https://seaborn.pydata.org/installing.html)**  

**sentdex_stock_market_episode12.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_stock_market_episode12.py) it needs:  
-   **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**  
-   **[Yahoo Index](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/YAHOO_INDEX_GSPC.csv)**  

**sentdex_visualization_episode13.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_visualization_episode13.py) it needs:  
-   **[matplotlib](https://matplotlib.org/)**  
-   **[seaborn](https://seaborn.pydata.org/installing.html)**  

**sentdex_prediction_episode15.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_prediction_episode15.py) it needs:       
-   **[Stock_market_full.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_full.csv)**      

**sentdex_getData_episode17.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_getData_episode17.py) it needs:     
-   **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**     

**sentdex_data_episode18.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_data_episode18.py) it needs:   
-   **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**   
-   **[Yahoo Index](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/YAHOO_INDEX_GSPC.csv)**   
-   **[Stock prices](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/stock_prices.zip)**  

**sentdex_data_episode19.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_prediction_episode19.py) it needs:   
-   **[Stock_market_acc_WITH_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_acc_WITH_NA.csv)**    
-   **[Stock_market_acc_NO_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_acc_NO_NA.csv)**     

**sentdex_data_episode20.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_profit_episode20.py) it needs:   
-   **[Stock_market_acc_WITH_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_acc_WITH_NA.csv)**    
-   **[Stock_market_acc_NO_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_acc_NO_NA.csv)**    

**sentdex_data_episode21.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_data_21.py) it needs:   
-   **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**      
 

**sentdex_data_episode22.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_data_episode22.py) it needs:   
-   **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**   
-   **[html yahoo current stock](https://drive.google.com/drive/folders/1gCjk0cv28Lu1ooYPe2X7j0c-2xT0HDBc?usp=sharing)**
  
**sentdex_data_episode23.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_prediction_episode23.py) it needs:   
-   **[Stock_market_acc_WITH_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_acc_WITH_NA.csv)**    
-   **[Stock_market_acc_NO_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/Stock_market_acc_NO_NA.csv)**
-   **[forward_sample_NO_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/forward_sample_NO_NA.csv)**    
-   **[forward_sample_With_NA.csv](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/forward_sample_WITH_NA.csv)**

**sentdex_data_episode24.py** can be found [here](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/source/sentdex_data_episode24.py) it needs:   
-   **[intraQuarter](https://pythonprogramming.net/downloads/intraQuarter.zip/)**   
-   **[Yahoo Index](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/YAHOO_INDEX_GSPC.csv)**   
-   **[Stock prices](https://github.com/LuposX/sentdex_fixed_market_stock/blob/master/datasets/stock_prices.zip)**  
  
</details> 

## License & Credits

MIT License means: [Click me](https://choosealicense.com/licenses/mit/)   
Credits sentdex: [Click me](https://www.youtube.com/user/sentdex/)  
