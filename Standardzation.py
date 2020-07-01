#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


data = pd.read_csv('homework2.csv')
data.head()


# In[45]:


data = data.drop('id', axis=1)
data['diagnosis'] = data['diagnosis'].factorize()[0]
data = data.fillna(value=0)
target = data['diagnosis']
data = data.drop('diagnosis', axis=1)
data.head()


# In[39]:


from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


# In[40]:


X = data.values

pca = PCA(n_components=2)
pca_2d = pca.fit_transform(X)

tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=2000)
tsne_results = tsne.fit_transform(X)


# In[41]:


plt.figure(figsize=(16,11))
plt.subplot(121)
plt.scatter(pca_2d[:,0], pca_2d[:,1], c=target, cmap="coolwarm", edgecolor="None", alpha=0.35)
plt.colorbar()
plt.title('PCA Scatter Plot')
plt.subplot(122)
plt.scatter(tsne_results[:,0], tsne_results[:,1], c=target, cmap = "coolwarm", edgecolor="None", alpha=0.35)
plt.colorbar()
plt.title('TSNE Scatter Plot')
plt.show()


# In[47]:


from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)


# In[26]:


pca = PCA(n_components=2)
pca_2d_std = pca.fit_transform(X_std)

tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=2000)
tsne_results_std = tsne.fit_transform(X_std)


# In[27]:


plt.figure(figsize = (16,11))
plt.subplot(121)
plt.scatter(pca_2d_std[:,0],pca_2d_std[:,1], c = target, 
            cmap = "RdYlGn", edgecolor = "None", alpha=0.35)
plt.colorbar()
plt.title('PCA Scatter Plot')

plt.subplot(122)
plt.scatter(tsne_results_std[:,0],tsne_results_std[:,1],  c = target, 
            cmap = "RdYlGn", edgecolor = "None", alpha=0.35)
plt.colorbar()
plt.title('TSNE Scatter Plot')
plt.show()


# In[28]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)

ypca_kmeans = kmeans.fit_predict(pca_2d)

plt.figure(figsize=(16,11))
plt.subplot(121)
sns.scatterplot(pca_2d[ypca_kmeans==0,0], pca_2d[ypca_kmeans ==0,1], color = 'yellow', label='Cluster 1 ', s=50)
sns.scatterplot(pca_2d[ypca_kmeans==1,0], pca_2d[ypca_kmeans ==1,1], color = 'blue', label='Cluster 2 ', s=50)
sns.scatterplot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'red', 
                label = 'Centroids',s=300,marker=',')

plt.grid(False)
plt.title('PCA')
plt.legend()
plt.show()

ytsne_kmeans = kmeans.fit_predict(tsne_results)

plt.figure(figsize=(16,11))
plt.subplot(122)
sns.scatterplot(tsne_results[ytsne_kmeans==0,0], tsne_results[ytsne_kmeans ==0,1], color = 'yellow', label='Cluster 1 ', s=50)
sns.scatterplot(tsne_results[ytsne_kmeans==1,0], tsne_results[ytsne_kmeans ==1,1], color = 'blue', label='Cluster 2 ', s=50)
sns.scatterplot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'red', 
                label = 'Centroids',s=300,marker=',')

plt.grid(False)
plt.title('TSNE')
plt.legend()
plt.show()


# In[29]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)

ypca_std_kmeans = kmeans.fit_predict(pca_2d_std)

plt.figure(figsize=(16,11))
plt.subplot(121)
sns.scatterplot(pca_2d_std[ypca_std_kmeans==0,0], pca_2d_std[ypca_std_kmeans ==0,1], color = 'yellow', label='Cluster 1 ', s=50)
sns.scatterplot(pca_2d_std[ypca_std_kmeans==1,0], pca_2d_std[ypca_std_kmeans ==1,1], color = 'blue', label='Cluster 2 ', s=50)
sns.scatterplot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'red', 
                label = 'Centroids',s=300,marker=',')

plt.grid(False)
plt.title('PCA')
plt.legend()
plt.show()

ytsne_std_kmeans = kmeans.fit_predict(tsne_results_std)

plt.figure(figsize=(16,11))
plt.subplot(122)
sns.scatterplot(tsne_results_std[ytsne_std_kmeans==0,0], tsne_results_std[ytsne_std_kmeans ==0,1], color = 'yellow', label='Cluster 1 ', s=50)
sns.scatterplot(tsne_results_std[ytsne_std_kmeans==1,0], tsne_results_std[ytsne_std_kmeans ==1,1], color = 'blue', label='Cluster 2 ', s=50)
sns.scatterplot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'red', 
                label = 'Centroids',s=300,marker=',')

plt.grid(False)
plt.title('TSNE')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




