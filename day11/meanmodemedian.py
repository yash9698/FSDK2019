# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:33:15 2019

@author: HP
"""

from scipy import stats
import numpy as np
x=np.array([13, 18, 13, 14, 13, 16, 14, 21, 13])
s=x.sum()
mean_=x.mean()
median=np.median(x)
range1=x.max()-x.min()
print("mean",mean_)
print("median",median)
print("range",range1)

print("mode",stats.mode(x))


