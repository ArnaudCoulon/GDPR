"""
Automate deleting files after a review
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*

import os
from os.path import *
import pandas as pd

#Reading the working file generated with inventory.py

df = pd.read_excel(path)

i = 0

#If columns E is True, delete file

while i < len(df["E"]):
    if df["E"][i] == True:
        os.remove(df["C"][i])
    i+=1
    
