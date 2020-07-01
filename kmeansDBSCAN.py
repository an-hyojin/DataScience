#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(context="notebook", palette="Spectral", style="darkgrid", font_scale=1.5, color_codes =True)


# In[3]:


dataset = pd.read_csv('input.csv', index_col='CustomerID')


# In[4]:


dataset.head()


# In[5]:


dataset.info()


# In[6]:


dataset.describe()


# In[7]:


dataset.isnull().sum()


# In[8]:


dataset.drop_duplicates(inplace=True)


# In[9]:


X = dataset.iloc[:,[2,3]].values


# In[10]:


from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters= i, init = 'k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


# In[11]:


plt.figure(figsize=(10,5))
sns.lineplot(range(1,11), wcss,marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[12]:


kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)


# In[13]:


plt.figure(figsize=(15,7))
sns.scatterplot(X[y_kmeans==0,0], X[y_kmeans ==0,1], color = 'yellow', label='Cluster 1 ', s=50)
sns.scatterplot(X[y_kmeans==1,0], X[y_kmeans ==1,1], color = 'blue', label='Cluster 2 ', s=50)
sns.scatterplot(X[y_kmeans==2,0], X[y_kmeans ==2,1], color = 'green', label='Cluster 3 ', s=50)
sns.scatterplot(X[y_kmeans==3,0], X[y_kmeans ==3,1], color = 'grey', label='Cluster 4 ', s=50)
sns.scatterplot(X[y_kmeans==4,0], X[y_kmeans ==4,1], color = 'orange', label='Cluster 5 ', s=50)
sns.scatterplot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'red', 
                label = 'Centroids',s=300,marker=',')
plt.grid(False)
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# In[42]:


from sklearn.cluster import DBSCAN
db = DBSCAN(eps=10, min_samples=8, metric='euclidean')
y_db = db.fit_predict(X)


plt.figure(figsize=(15,7))

sns.scatterplot(X[y_db==0,0], X[y_db ==0,1], color = 'yellow', label='Cluster 1 ', s=50)
sns.scatterplot(X[y_db==1,0], X[y_db ==1,1], color = 'blue', label='Cluster 2 ', s=50)
sns.scatterplot(X[y_db==2,0], X[y_db ==2,1], color = 'green', label='Cluster 3 ', s=50)
sns.scatterplot(X[y_db==3,0], X[y_db ==3,1], color = 'grey', label='Cluster 4 ', s=50)
sns.scatterplot(X[y_db==4,0], X[y_db ==4,1], color = 'orange', label='Cluster 5 ', s=50)

plt.grid(False)
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# In[ ]:




