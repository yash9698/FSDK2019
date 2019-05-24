# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:01:19 2019

@author: HP
"""



import mysql.connector
from pandas import DataFrame
conn = mysql.connector.connect ( user='root', password='', host='localhost')


c = conn.cursor()
c.execute("CREATE DATABASE stu1;")
c.execute("USE stu1;")
c.execute ("""CREATE TABLE student(
          age INTEGER,
          branch  TEXT,
          name TEXT,
          roll INTEGER
          )""")


c.execute("INSERT INTO student VALUES (20,'it', 'yash gupta', 91)")
c.execute("INSERT INTO student VALUES (21,'it', 'tarun josji', 88)")
c.execute("INSERT INTO student VALUES (19,'it', 'utkarsh sharma', 89)")
c.execute("INSERT INTO student VALUES (22,'it', 'prajjawal kansal', 58)")
c.execute("INSERT INTO student VALUES (20,'it', 'samarth chadda', 70)")

c.execute("SELECT * FROM student")
# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["age","branch","name","roll"]
conn.commit()

# STEP 7
# closing the connection 
conn.close()