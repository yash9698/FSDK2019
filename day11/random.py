# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:20:31 2019

@author: HP
"""

import numpy as np
import random
from scipy import stats
array=np.random.randint(5,15,40)
print(array)
print("most frequent value is: ",stats.mode(array)[0])