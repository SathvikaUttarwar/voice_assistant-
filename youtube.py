#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
class music():
    def __init__(self):
        service = Service(r"C:\Users\sathv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service) 
    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video=self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        video.click()

assist=music()
assist.play('dynamite by bts')
        


# In[ ]:




