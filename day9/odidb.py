# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:40:55 2019

@author: HP
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
#import urllib



#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
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
df.to_csv("team_data.csv")
import os
import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'odi.db' )
c.execute ("""CREATE TABLE rank(
          pos TEXT,
          team_name  TEXT,
          w_match TEXT,
          points TEXT,
          rating  TEXT
          )""")

c = conn.cursor()
for i in range(0,len(B)):
    c.execute("INSERT INTO rank VALUES ('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))



c.execute("SELECT * FROM rank")
# STEP 6
df1 = DataFrame(c.fetchall())  # putting the result into Dataframe
df1.columns = ["pos","team_name","w_match","points","rating"]
conn.commit()

# STEP 7
# closing the connection 
conn.close()
