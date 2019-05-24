# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:44:06 2019

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Telecom_churn.csv")
df1=df.loc[(df['international plan'] =='yes') & \
           (df['voice mail plan'] == 'yes' ) & \
           (df['churn']==True)]
count=df1.count()[4]
print("customer on both international and voice mail plan",count)
s=df['total intl charge'].loc[(df['churn']==True)]
s1=df['total intl charge'].loc[(df['churn']==False)]
churn=s.sum()
nchurn=s1.sum()
labels = 'CHURN', 'NONCHURN'
sizes = [churn,nchurn]
colors = ['gold', 'yellowgreen']
explode = ( 0, 0)  # explode 1st slice

#plt.pie(sizes, labels=labels, autopct='%.0f%%')

# or

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
d=df.loc[(df['churn']==True)]
m=d['total night minutes'].max()
print(d['state'].loc[(d['total night minutes']==m)])

