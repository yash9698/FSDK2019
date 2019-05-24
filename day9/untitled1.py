# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:35:06 2019

@author: HP
"""


import os
import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'studd.db' )
c.execute ("""CREATE TABLE studentsss(
          age INTEGER,
          branch  TEXT,
          name TEXT,
          roll INTEGER
          )""")

c = conn.cursor()

c.execute("INSERT INTO studentsss VALUES (20,'it', 'yash gupta', 91)")
c.execute("INSERT INTO studentsss VALUES (21,'it', 'tarun josji', 88)")
c.execute("INSERT INTO studentsss VALUES (19,'it', 'utkarsh sharma', 89)")
c.execute("INSERT INTO studentsss VALUES (22,'it', 'prajjawal kansal', 58)")
c.execute("INSERT INTO studentsss VALUES (20,'it', 'samarth chadda', 70)")

c.execute("SELECT * FROM studentsss")
# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["age","branch","name","roll"]
 conn.commit()

# STEP 7
# closing the connection 
conn.close()