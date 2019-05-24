# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:50:02 2019

@author: Tarun Joshi
"""

users = {} 
with open('passwd') as f:
    for line in f:
        if not line.startswith("#"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
 
for username in sorted(users):
    print("{}:{}".format(username, users[username]))