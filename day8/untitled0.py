# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:24:46 2019

@author: HP
"""

"""
Created on Wed May 15 17:36:36 2019
@author: Tarun Joshi
"""
# Bid Plus
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver.exe")

browser.get(url)

sleep(2)
 
#school_code = browser.find_element_by_name("treg")
#code="2000"
#school_code.send_keys(code)
#
#
#sleep(2)
for i in range(1,3):
    get_school_result = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    get_school_result.click()
    sleep(5)
 
html_page = browser.page_source
soup = BS(html_page)

sleep(3)

browser.quit()
