# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:06:44 2019

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Automobile.csv")
series = df["make"].value_counts()

print (series.index[0:11])
print (series.values[0:11])

explode = (0.5,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()