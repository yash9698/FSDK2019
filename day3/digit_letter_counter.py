# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:28:48 2019

@author: Tarun Joshi
"""

#Digit Letter Counter

digits=0
letters=0
str1=input("enter the string")
for x in str1:
    if x.isdigit():
        digits=digits+1
    elif x.isalpha():
        letters=letters+1
    else:
        continue
print(digits)
print(letters)