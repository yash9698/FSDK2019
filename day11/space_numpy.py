# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:02:31 2019

@author: HP
"""
import numpy as np
list2=[]
x=input("enter 9 element of list")
list1=x.split()
list1 = list(map(int, list1))
list2=np.array(list1)
list2 = list2.reshape(3,3)
print(list2)




    
