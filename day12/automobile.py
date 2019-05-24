# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:16:20 2019

@author: HP
"""

import pandas as pd
import numpy as np
df1 = pd.read_csv("Automobile1.csv")

df1['price'] = df1['price'].fillna(df1['price'].mean())
print(df1['price'])
price=df1['price']
numpyprice=np.array(price)
print(numpyprice)
mean=df1['price'].describe()[1]
minimum=df1['price'].describe()[3]
std=df1['price'].describe()[2]
maximum=df1['price'].describe()[7]
print("mean is",mean)
print("minimum is",minimum)
print("standard deviation is",std)
print("max is",maximum)