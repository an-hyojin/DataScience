#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

heart = pd.read_csv('heart.csv')
heart.info()


# In[2]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(heart.drop('target', 1), heart['target'], test_size=0.2, random_state=10)


# In[3]:


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(max_depth=5)
model.fit(X_train, y_train)


# In[4]:


from sklearn.metrics import accuracy_score
y_train_hat_dt = model.predict(X_train)
print('train accuracy: ', accuracy_score(y_train, y_train_hat_dt))
y_test_hat_dt = model.predict(X_test)
print('test accuracy: ' , accuracy_score(y_test, y_test_hat_dt))


# In[5]:


from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = SVC(C=100)
clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_train_hat = clf.predict(X_train_scaled)
print('train accuracy: ', accuracy_score(y_train, y_train_hat))
y_test_hat = clf.predict(X_test_scaled)
print('test accuracy: ' , accuracy_score(y_test, y_test_hat))


# In[6]:


from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print(confusion_matrix(y_test, y_test_hat))
print(classification_report(y_test, y_test_hat, target_names=['A', 'B']))
print(confusion_matrix(y_test, y_test_hat_dt))
print(classification_report(y_test, y_test_hat_dt, target_names=['A', 'B']))


# In[ ]:




