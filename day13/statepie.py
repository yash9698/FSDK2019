# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:27:22 2019

@author: HP
"""

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source=requests.get(url).text
soup=BeautifulSoup(source,"lxml")
_table=soup.find('table', class_='wikitable sortable')




#Generate lists
A=[]


E=[]
tb=_table.find('tbody')

for row in tb.findAll('tr'):
    cells = row.findAll('td')
    
    if len(cells)==7:

      A.append(cells[1].text.strip())
    
      E.append(cells[4].text.strip())
list1=A[:6]
list2=E[:6] 
labels = list1
sizes = list2
colors =['blue','green','red','yellow','black','pink']
explode = ( 0.2, 0,0,0,0,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)   
plt.axis('equal')
plt.show()

