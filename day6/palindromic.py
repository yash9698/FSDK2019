# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:18:47 2019

@author: HP
"""

list1=input("enter comma seperated integer")
lst=list1.split(",")
lst2=[]
for i in lst:
    if int(i)>0:
        lst2.append(True)
    else:
        lst2.append(False)

if all(lst2):
    s=any(list(map(lambda x: True if x==x[::-1]else False,lst)))
    print(s)
else:
    print( "False")    