# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:52:43 2019

@author: Tarun Joshi
"""

import csv

with open('passwd') as passwd, open('output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))