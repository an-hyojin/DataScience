#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn import linear_model
house = pd.read_csv('USA_Housing.csv')
house.info()


# In[2]:


sns.pairplot(house)#데이터 상관관계 분석


# In[3]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


linear_regression = linear_model.LinearRegression()
X = house[['Avg. Area Income']]
y = house['Price']

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.8, test_size=0.2)

slr = LinearRegression()
slr.fit(X_train.values.reshape(-1,1), y_train)

y_predicted = slr.predict(X_test)
plt.scatter(y_test, y_predicted)
plt.xlabel("Actual Price")
plt.ylabel("Predict Price")
plt.show()

print(slr.score(X_test,y_test))#R제곱


# In[4]:


mlr_X = house[['Avg. Area Income', 'Avg. Area House Age','Area Population']]
mlr_Y = house[['Price']]
mlrx_train, mlrx_test, mlry_train, mlry_test = train_test_split(mlr_X, mlr_Y, train_size=0.8, test_size=0.2)

mlr = LinearRegression()
mlr.fit(mlrx_train, mlry_train)

mlry_predict = mlr.predict(mlrx_test)

plt.scatter(mlry_test, mlry_predict)
plt.xlabel("Actual Price")
plt.ylabel("Predict Price")
plt.show()

print(mlr.score(mlrx_test,mlry_test))


# In[ ]:





# In[ ]:




