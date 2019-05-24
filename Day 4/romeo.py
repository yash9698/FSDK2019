# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:46:20 2019

@author: Tarun Joshi
"""

with open("romeo.txt", "rt") as fileobj:

    content = fileobj.readlines()
    
    req_content = []
    for var in content:
        req_content.append(var.split())
    
    dict1 = {}
    for var2 in req_content:
        for var3 in var2:
            if var3 not in dict1:
                dict1[var3] = 1
            else:
                dict1[var3]+=1
