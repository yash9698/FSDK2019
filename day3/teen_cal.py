# -*- coding: utf-8 -*-
"""
Created on Mon May 20 01:07:20 2019

@author: Tarun Joshi
"""

def fix_teen(number):
    teen_list = [13,14,17,18,19]
    if number in teen_list:
        return 0
    else:
        return number
def no_teen_sum ( dictionary ):
    list_of_numbers = dictionary.values()
    Sum = 0
    for number in list_of_numbers:
        Sum += fix_teen ( number )
    return Sum


user_input = input("Enter the dictionary input")

splitted_string = user_input.split(',')


splitted_string[0] = splitted_string[0][1:]
splitted_string[len(splitted_string)-1] =splitted_string[len(splitted_string)-1][0:-1] 

dictionary = {}
for i in splitted_string:
    i = i.split(':')
    i[0] = i[0].replace('"','')
    i[1] = int(i[1])
    dictionary[i[0]] = i[1]

print("Sum = " + str(no_teen_sum ( dictionary )))