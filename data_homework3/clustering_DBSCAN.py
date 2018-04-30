# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:36:48 2018

@author: lmy
"""

import pandas as pd
import numpy as np
import data_preprocess as pp
from sklearn.cluster import DBSCAN  
from sklearn import metrics  
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  

data = pd.read_csv('./train.csv')
X = pp.characterize(data)[['Sex','Age','Fare']]
y = data['Survived']

#对数据进行标准化  
X = StandardScaler().fit_transform(X)  
  
#计算  
db = DBSCAN(eps=0.3,min_samples=10).fit(X)  
core_samples_mask = np.zeros_like(db.labels_,dtype=bool)  
core_samples_mask[db.core_sample_indices_] = True  
labels = db.labels_  
  
n_clusters_ = len(set(labels))-(1 if -1 in labels else 0)  
  
unique_labels = set(labels)  
colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))  
for k,col in zip(unique_labels,colors):  
    if k == -1:  
        col = 'k'  
    class_member_mask = (labels == k)  
    xy = X[class_member_mask & core_samples_mask]  
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,  
             markeredgecolor='k', markersize=14)  
  
    xy = X[class_member_mask & ~core_samples_mask]  
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,  
             markeredgecolor='k', markersize=6)  
  
plt.title('Estimated number of clusters: %d' % n_clusters_)  
plt.show()

