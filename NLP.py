#!/usr/bin/env python
# coding: utf-8

# In[1]:


import konlpy
import pandas as pd
import re
import csv
from konlpy.tag import Kkma
from konlpy.tag import Okt
from konlpy.utils import pprint
from konlpy.tag import Hannanum
from collections import Counter
kkma = Kkma()
hannanum = Hannanum()


# In[2]:


kkmaRes = []
oktRes = []
with open('allSong.csv') as data:
    csv_reader = csv.reader(data)
    next(csv_reader) # 헤더 읽음 처리
    for song in csv_reader:
        for line in song[2].split("\n"):
            # pprint(kkma.pos(line))
            if len(line.strip())==0:
                continue
            print(line)
#             pprint(kkma.morphs(line))
#             pprint(okt.morphs(line))
#             kkmaRes.extend(kkma.morphs(line))
#             oktRes.extend(okt.morphs(line))
            # pprint(hannanum.nouns(line))
            # pprint(hannanum.pos(line))
        break
            


# In[3]:


kVocab = Counter(kkmaRes)
print(kVocab)


# In[4]:


oVocab = Counter(oktRes)
print(oVocab)


# In[14]:


dic = {}
regex = re.compile('[0-9]') # 가다01 가다02 이런식으로 되어있는 것들 제거하기 위함

with open('words.csv') as data:
    csv_reader = csv.reader(data)
    next(csv_reader) # 헤더 읽음 처리
    for word_list in csv_reader:
        word = word_list[1]
        num = regex.search(word)
        if num : #num이 들어가있으면 제거
            word = word[0:num.start()]
        dic[word] = word_list[4]
        print(word_list[4])


# In[9]:


song_list = {}
song_lyrics = {}
kor_rex = re.compile('[가-힣]+') #한글만 볼 것
from termcolor import colored
okt = Okt()
with open('allSong.csv') as data:
    csv_reader = csv.reader(data)
    
    next(csv_reader) # 헤더 읽음 처리
    for song in csv_reader:
        words = []
        lyric = []
        for line in kkma.sentences(song[2]):
            # pprint(kkma.pos(line)) 
            for word in okt.morphs(line):
                if bool(re.search(kor_rex, word)):
                    lyric.append(word)
                if word in dic:
                    words.append(word)
                    print(colored(word,'red'), end=' ')
                    continue
                print(word, end=' ') 
            print()
        song_lyrics[song[0]+"-"+song[1]] = lyric
        song_list[song[0]+"-"+song[1]] = words


# In[10]:


for k in song_list:
    print(k)
    for word in song_list[k]:
        if word in dic:
            print(word, end=' ')
            
    print()


# In[11]:


stopwords = []
with open('stopwords.csv') as data:
    csv_reader = csv.reader(data)
    next(csv_reader)
    for stopword in csv_reader:
        stopwords.extend(stopword)
        print(stopword)

        
    


# In[12]:


print(stopwords)


# In[13]:


from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer(stop_words = stopwords)


# In[ ]:


for l in song_lyrics:
    print()
    vect.fit_transform(song_lyrics[l])
    print(vect.vocabulary_)


# In[ ]:




