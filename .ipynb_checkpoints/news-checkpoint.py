#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
from ss import *
api_address = "https://newsapi.org/v2/top-headlines?country=us&apikey="+'8b9965ab48f34599aa55b41c8b48f678'
json_data = requests.get(api_address).json()



ar = []
def news():
    num_articles = min(3, len(json_data["articles"]))
    for i in range(num_articles):
        ar.append("Number " + str(i+1) + ": " + json_data["articles"][i]["title"] + ".")
    return ar
ar = news()
print(ar)





# In[ ]:




