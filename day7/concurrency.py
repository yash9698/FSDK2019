# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:27:57 2019

@author: HP
"""

import requests
usd=int(input("Enter value in USD"))
url1 = "https://free.currconv.com/api/v7/convert?q=USD_inr&compact=ultra&apiKey=5c0fc5a141ebb82b583b"
response = requests.get(url1)
print(response.content)
jsondata = response.json()
print(jsondata["USD_INR"]*usd)