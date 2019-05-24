# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:51:10 2019

@author: HP
"""

import pandas as pd
df1=pd.DataFrame(columns=['NAME','SEX','NUMBER','YEAR'])
for i in range(1880,2011):
    filename="yob"+str(i)+".txt"
    df2=pd.read_csv(filename,header=None)
    df2.columns=['NAME','SEX','NUMBER']
    df2["YEAR"]=i
    df2.sort_values(by=["NUMBER"],ascending=False)
    df1=pd.concat([df1,df2])
print("top 5 male in 2010 \n",df1[(df1["SEX"]=='M')&(df1["YEAR"]==2010)].head())    
print("top 5 female in 2010 \n",df1[(df1["SEX"]=='F')&(df1["YEAR"]==2010)].head()) 
df=df1.groupby(["YEAR","SEX"])["NUMBER"].aggregate("sum").unstack()
df.plot()    