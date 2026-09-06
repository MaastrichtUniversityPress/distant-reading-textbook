# Script for writing tweets collected with the Web Data Research Assistant (developed by Leslie Carr) in multiple HTML files
# to separate EXCEL files (removing tweets that contain no actual text)

# import packages
import pandas as pd
import numpy as np
from urllib.parse import urljoin
import os

# define file path for output data

outpath = "C:\\Users\\mobarget\\Downloads\\"

# files collected with WDRA and stored on Github

filenames= ("WebDataRA-2022-09-21T11_52_44.html",
    "WebDataRA-2022-09-21T11_54_00.html",
    "WebDataRA-2022-09-21T11_55_33.html",
    "WebDataRA-2022-09-21T11_59_16.html",
    "WebDataRA-2022-09-21T12_07_45.html",
    "WebDataRA-2022-09-21T12_08_42.html",
    "WebDataRA-2022-09-21T12_10_20.html",
    "WebDataRA-2022-09-21T12_15_34.html",
    "WebDataRA-2022-09-21T12_16_50.html",
    "WebDataRA-2022-09-21T12_17_43.html",
    "WebDataRA-2022-09-21T12_18_29.html",
    "WebDataRA-2022-09-21T12_19_25.html",
    "WebDataRA-2022-09-21T12_20_53.html",
    "WebDataRA-2022-09-21T12_21_46.html",
    "WebDataRA-2022-09-21T12_23_01.html",
    "WebDataRA-2022-09-21T12_24_06.html",
    "WebDataRA-2022-09-21T12_25_53.html",
    "WebDataRA-2022-09-21T12_26_53.html",
    "WebDataRA-2022-09-21T12_27_19.html",
    "WebDataRA-2022-09-21T12_28_28.html",
    "WebDataRA-2022-09-21T12_28_50.html",
    "WebDataRA-2022-09-21T12_30_41.html",
    "WebDataRA-2022-09-21T12_31_38.html",
    "WebDataRA-2022-09-21T12_32_47.html",
    "WebDataRA-2022-09-21T12_33_18.html",
    "WebDataRA-2022-09-21T12_34_00.html",
    "WebDataRA-2022-09-21T12_34_20.html",
    "WebDataRA-2022-09-21T12_34_49.html",
    "WebDataRA-2022-09-21T12_35_04.html",
    "WebDataRA-2022-09-21T12_36_33.html",
    "WebDataRA-2022-09-21T12_37_04.html",
    "WebDataRA-2022-09-21T12_37_30.html",
    "WebDataRA-2022-09-21T12_38_54.html",
    "WebDataRA-2022-09-21T12_39_10.html",
    "WebDataRA-2022-09-21T12_40_14.html",
    "WebDataRA-2022-09-21T12_40_42.html",
    "WebDataRA-2022-09-21T12_41_56.html",
    "WebDataRA-2022-09-21T12_42_52.html",
    "WebDataRA-2022-09-21T12_44_05.html",
    "WebDataRA-2022-09-21T12_45_28.html",
    "WebDataRA-backup-1000.html")
  
# create URL for each file whose table we want to extract

path="https://raw.githubusercontent.com/MonikaBarget/DistantReading/main/VMA2013_tweets/"

counter=0
for f in filenames:
    url=urljoin(path, f)
    print(url)
    counter+= 1
    
# assign the table data to a Pandas dataframe
    table = pd.read_html(url)[0] 
    print(table)
    
# delete rows where text cell is empty    
    
    table['Text'].replace('', np.nan, inplace=True)
    table.dropna(subset=['Text'], inplace=True)
    
    outfile=os.path.join(outpath, str(counter) + ".xlsx")
    print(outfile)
    
# store the dataframe in NEW Excel file
    
    table.to_excel(outfile)
    
print("done")
