#!/usr/bin/env python
# coding: utf-8

# In[10]:


from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome('/Users/hyojin/Desktop/chromedriver') #드라이버 설정
url = 'https://vibe.naver.com/chart/total'# 크롤링할 url
browser.get(url)
browser.implicitly_wait(10) # 기다리는 시간 설정


# In[11]:


import time
btn = browser.find_element_by_css_selector("#app > div.modal > div > div > a") # 광고 창 삭제 버튼
btn.click() #삭제 클릭
time.sleep(1) #삭제 기다리기


# In[12]:


ranking_table = browser.find_element_by_css_selector("#content > div.track_section > div:nth-child(1) > div > table > tbody")
# 순위 목록 테이블
rows = ranking_table.find_elements_by_tag_name("tr") # 순위들 리스트로 가져옴
matrix =[]
head = ["Singer","Title", "Lyrics"]
matrix.append(head)
initial_scroll=0
next_scroll = 51


# In[13]:


for row in rows:
    lylics_td=row.find_elements_by_css_selector(".lyrics")[0] # 가사 있는 cell
    if len(lylics_td.find_elements_by_tag_name("a"))>0: # 가사가 있을 경우
        lylics_td.find_elements_by_tag_name("a")[0].click() # 가사 보기 버튼 클릭
        time.sleep(1) # 로딩 기다리기
        title = browser.find_elements_by_xpath("//*[@id='app']/div[2]/div/div/div[1]/div[2]/div/strong")[0].text;
        singer = browser.find_elements_by_xpath("//*[@id='app']/div[2]/div/div/div[1]/div[2]/div/em")[0].text;
        lylics = browser.find_elements_by_css_selector("#app > div.modal > div > div > div.ly_contents > p > span:nth-child(2)")[0].text;
        
        data = []
        data.append(singer[5:].strip())
        data.append(title[2:].strip())
        data.append(lylics.strip())
        matrix.append(data)
        close_btn = browser.find_elements_by_css_selector("#app > div.modal > div > div > a")[0].click() # 가사 창닫기
        
    
    scroll_command = "window.scrollTo(0,"+str(next_scroll)+");" # 화면 스크롤
    browser.execute_script(scroll_command)
    initial_scroll = next_scroll;
    next_scroll += 51;
    


# In[16]:


import pandas as pd
df = pd.DataFrame(matrix)
df.to_csv("song.csv",header=None, index=None) # csv파일로 변환


# In[ ]:




