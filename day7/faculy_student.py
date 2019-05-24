# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:08:24 2019

@author: HP
"""
import json
faculty=[{
	
	  "first name" :"tarun",
      "last name":"joshi",
      "photo":"https://www.bing.com/images/search?view=detailV2&ccid=67GWX3c9&id=3C3B8967BE1FC288E4CEE272D7F317A15A1F1B0A&thid=OIP.67GWX3c9yKlH0IfEAsIBLQHaFj&mediaurl=http%3a%2f%2f1.bp.blogspot.com%2f-3th9JH-VS1A%2fUS100_ExuKI%2fAAAAAAAADmE%2fcKl6zYHWaQg%2fs1600%2fCamellia-flower.jpg&exph=768&expw=1024&q=photos+of+flower&simid=608029812976648682&selectedIndex=1&ajaxhist=0",
      "department":"CSE",
      "researce_Areas":["youtubers","physics"],
      "contact_details":[
      {"mobile_no":132627383939,
      "email":"abc@gmail.com"
      }]
},
 {
	
	  "first name" :"prajjawal",
      "last name":"kansal",
      "photo":"https://www.bing.com/images/search?view=detailV2&ccid=67GWX3c9&id=3C3B8967BE1FC288E4CEE272D7F317A15A1F1B0A&thid=OIP.67GWX3c9yKlH0IfEAsIBLQHaFj&mediaurl=http%3a%2f%2f1.bp.blogspot.com%2f-3th9JH-VS1A%2fUS100_ExuKI%2fAAAAAAAADmE%2fcKl6zYHWaQg%2fs1600%2fCamellia-flower.jpg&exph=768&expw=1024&q=photos+of+flower&simid=608029812976648682&selectedIndex=1&ajaxhist=0",
      "department":"CSE",
      "researce_Areas":["stud","girls"],
      "contact_details":[
      {"mobile_no":132627383939,
      "email":"abc@gmail.com"
      }]
}]

student=[{
	
	  "first name" :"tarun",
      "last name":"joshi",
      "photo":"https://www.bing.com/images/search?view=detailV2&ccid=67GWX3c9&id=3C3B8967BE1FC288E4CEE272D7F317A15A1F1B0A&thid=OIP.67GWX3c9yKlH0IfEAsIBLQHaFj&mediaurl=http%3a%2f%2f1.bp.blogspot.com%2f-3th9JH-VS1A%2fUS100_ExuKI%2fAAAAAAAADmE%2fcKl6zYHWaQg%2fs1600%2fCamellia-flower.jpg&exph=768&expw=1024&q=photos+of+flower&simid=608029812976648682&selectedIndex=1&ajaxhist=0",
      "branch":"CSE",
      "interest":["youtubers","physics"],
      "contact_details":[
      {"mobile_no":132627383939,
      "email":"abc@gmail.com"
      }]
},
 {
	
	  "first name" :"prajjawal",
      "last name":"kansal",
      "photo":"https://www.bing.com/images/search?view=detailV2&ccid=67GWX3c9&id=3C3B8967BE1FC288E4CEE272D7F317A15A1F1B0A&thid=OIP.67GWX3c9yKlH0IfEAsIBLQHaFj&mediaurl=http%3a%2f%2f1.bp.blogspot.com%2f-3th9JH-VS1A%2fUS100_ExuKI%2fAAAAAAAADmE%2fcKl6zYHWaQg%2fs1600%2fCamellia-flower.jpg&exph=768&expw=1024&q=photos+of+flower&simid=608029812976648682&selectedIndex=1&ajaxhist=0",
      "branch":"CSE",
      "interest":["stud","girls"],
      "contact_details":[
      {"mobile_no":132627383939,
      "email":"abc@gmail.com"
      }]
}]
file1=json.dumps(faculty) 
file2=json.dumps(student)  
with open("st.json","wt")as fp:
      json.dump(file2,fp)    
with open("ft.json","wt")as fp:
      json.dump(file1,fp)             