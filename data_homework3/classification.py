# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 10:38:16 2018

@author: lmy
"""

import pandas as pd
import data_preprocess as pp
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

data = pd.read_csv('./train.csv')
X = pp.characterize(data)
y = data['Survived']
#validation set
train_x,test_x,train_y,test_y = train_test_split(X,y,test_size = 0.25,random_state = 33)

#classication 1: LogisticRegression
clf_LR = LogisticRegression(C = 1.0,penalty = 'l1',tol = 1e-6)
clf_LR.fit(train_x,train_y)
print(clf_LR)
predict_LR = clf_LR.predict(test_x)
accuracy = clf_LR.score(test_x,test_y)
print("accuracy:",accuracy)
report = classification_report(predict_LR,test_y,target_names = ['died 0','survive 1'])
print(report)

#classication 2: svm
from sklearn import svm
clf_svm = svm.SVC()
clf_svm.fit(train_x,train_y)
print(clf_svm)
predict_svm = clf_svm.predict(test_x)
accuracy_svm = clf_svm.score(test_x,test_y)
print("accuracy:",accuracy_svm)
#test_y = map(lambda x: int(x), test_y)
#predict_svm = pd.Series(predict_svm).apply(lambda x : 1 if x>=0.5 else 0)
report_svm = classification_report(predict_svm,test_y,target_names = ['died 0','survive 1'])
print(report_svm)

##classication 3: DecisionTree
from sklearn import tree
dt=tree.DecisionTreeClassifier()
dt=dt.fit(train_x,train_y)
print(dt)
accuracy_dt = dt.score(test_x, test_y)
print("accuracy:",accuracy_dt)
predict_dt = dt.predict(test_x)
print(classification_report(predict_dt, test_y, target_names = ['died 0', 'survived 1']))
