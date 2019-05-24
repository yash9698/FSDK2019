# -*- coding: utf-8 -*-
"""
Created on Mon May 20 01:10:05 2019

@author: Tarun Joshi
"""

user_input = input("Enter String: ")

character_frequency = {}      

for alphabet in user_input:
    character_frequency[alphabet] = character_frequency.get(alphabet,0) + 1
    
print (character_frequency)