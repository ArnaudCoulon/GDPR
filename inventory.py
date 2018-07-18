#import libraries
import os
from os.path import *
import pandas as pd
from datetime import datetime

path = yourpath
df = pd.DataFrame(columns=list("ABCD"))

#loop walking throught the path. Get Name, last modification date, dir and size' file

for root,dirs,files in os.walk(path):
    for file in files:

        chemin = join(root,file)
        df = df.append(pd.DataFrame({"A" :[file],"B" :[datetime.fromtimestamp(os.path.getctime(chemin)).strftime('%d/%m/%Y')], "C" : [chemin],"D" : [os.path.getsize(chemin)]}))


#Loading in an Excel file
df.to_excel("C:/Users/984098/Desktop/rgpd.xlsx")
