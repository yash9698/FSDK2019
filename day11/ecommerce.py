# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:54:35 2019

@author: HP
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes) 
plt.hist(incomes,normed=True,bins=50)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
incomes = np.append(incomes, [10000000000])
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))