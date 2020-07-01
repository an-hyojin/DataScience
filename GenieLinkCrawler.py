#!/usr/bin/env python
# coding: utf-8

# In[33]:


import requests
from bs4 import BeautifulSoup

array = ['https://www.genie.co.kr/detail/songInfo?xgnm=87230562','https://www.genie.co.kr/detail/songInfo?xgnm=88040624','https://www.genie.co.kr/detail/songInfo?xgnm=86700924','https://www.genie.co.kr/detail/songInfo?xgnm=88740322','https://genie.co.kr/detail/songInfo?xgnm=86525645']
res = []
headers = {'User-Agent':""}# 헤더 설정
i =0
for url in array:
    req = requests.get(url, headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    my_titles = soup.select('#pLyrics > div')
    my_lylics = soup.select('#pLyrics > p')
    res.append([])
    res[i].append(my_titles[0].text)
    res[i].append(my_lylics[0].text)
    i= i+1
    
for a in res:
    print(a[0])
    print(a[1])


# In[17]:


my_titles = soup.select('#body-content > h2 > a')

print(my_titles[0].text)
my_lylics = soup.select('#pLyrics > p')

print(my_lylics[0].text)


# In[2]:


from selenium import webdriver
browser = webdriver.Chrome('Users/hyojin/chromedriver')
url = 'https://www.genie.co.kr/chart/top200'
browser.get(url)


# In[ ]:





# In[ ]:




