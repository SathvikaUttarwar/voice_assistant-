#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

url="http://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

arr=["",""]
arr[0]=json_data["setup"]
arr[1] = json_data["punchline"]
def joke():
    return arr


# In[ ]:




