#!/usr/bin/env python
# coding: utf-8

# In[16]:


import csv
import re

pattern = re.compile('[가-힣]+')


# In[17]:


def isHangel(str): # 한글이 몇 퍼센트의 비율로 들어가있는지 판단
    
    #  \n과 \s+ 제거
    lyrics = re.sub('\n',' ', str)
    lyrics = re.sub('\s+',' ',lyrics)
    
    lyricArray = lyrics.split(' ')
    hangel = 0
    
    for eachlyric in lyricArray:
        if bool(re.search(pattern, eachlyric)): # 한글 단어일 경우
            hangel = hangel + 1
    
    return hangel/len(lyricArray)


# In[21]:


songList = [] # 적합한 Song List 저장 위함
header=["Singer", "Title", "Lyrics"]

with open('allSong.csv') as data:
    csv_reader = csv.reader(data)
    next(csv_reader) # 헤더 읽음 처리
    for line in csv_reader:
        if isHangel(line[2])>=0.6: # 한글 비율이 0.6이상이면 적합하다고 판단
            songList.append(line)
            


# In[22]:


print(len(songList))
for line in songList:
    print(line[1])


# In[23]:


import pandas as pd
df = pd.DataFrame(songList)
df.to_csv("GoodSong.csv",header=None, index=None) # csv파일로 변환


# In[ ]:





# In[ ]:




