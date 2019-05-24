# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:04:22 2019

@author: YASH GUPTA
"""
import pymongo

client = pymongo.MongoClient("mongodb://yash123:Yash%40123@cluster0-shard-00-00-ji0e4.mongodb.net:27017,cluster0-shard-00-01-ji0e4.mongodb.net:27017,cluster0-shard-00-02-ji0e4.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.yash_db
def add_student(idd, first, last, pay):
    unique_student = mydb.student.find_one({"id":idd})
    if unique_student:
        return "Student already exists"
    else:
        mydb.student.insert(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Student added successfully"

def fetch_all_student():
    user = mydb.student.find()
    for i in user:
        print (i)


add_student('Tarun Joshi', 21, 1,'IT')
add_student('Yash Gupta',40,2,'IT')
add_student('Utkarsh Sharma', 21,3,'IT')
add_student('Prajjawal Kansal', 21,4,'IT')

