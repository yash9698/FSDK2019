# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:36:03 2019

@author: HP
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
#import urllib



#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")


_table=soup.find('table', class_='table')




#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
tb=_table.find('tbody')

for row in tb.findAll('tr'):
    cells = row.findAll('td')
    
    
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
    E.append(cells[4].text.strip())
    


col_name = ["position","team name","weighted match","point","rating",]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("team_data1.csv")
