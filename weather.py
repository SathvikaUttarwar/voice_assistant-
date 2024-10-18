#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from ss import *
api_address="http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid="+'406fc012b0c0cf08902977171aa260ee'
json_data=requests.get(api_address).json()

def temp():
    temprature = round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description = json_data["weather"][0]["description"]
    return description

print(temp())
print(des())



# In[ ]:




