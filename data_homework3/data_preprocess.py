# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:08:14 2018

@author: lmy
"""
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def miss_data_handle(df):
    age_predict_df = df[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
    known_age = age_predict_df[age_predict_df.Age.notnull()].as_matrix()
    unknown_age = age_predict_df[age_predict_df.Age.isnull()].as_matrix()
    
    # y即目标年龄
    y = known_age[:, 0]
    # X即特征属性值
    X = known_age[:, 1:]
    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])
    # 用得到的预测结果填补原缺失数据
    df.loc[ (df.Age.isnull()), 'Age' ] = predictedAges 
    
    df.loc[ (df.Cabin.notnull()), 'Cabin' ] = 1
    df.loc[ (df.Cabin.isnull()), 'Cabin' ] = 0
    return df

def characterize(df):
    df = miss_data_handle(df)
    #特征提取
    df.loc[df['Sex'] == 'male','Sex'] = 1
    df.loc[df['Sex'] == 'female','Sex'] = 0
    
    df.loc[df['Embarked'] == 'S','Embarked'] = 0
    df.loc[df['Embarked'] == 'C','Embarked'] = 1
    df.loc[df['Embarked'] == 'Q','Embarked'] = 2
    df.loc[(df['Embarked'].isnull()),'Embarked'] = 0
    
    feature_df = df[['Pclass','Sex','Age','SibSp','Parch','Fare','Cabin','Embarked']]
    
    #return feature_df.to_csv('./train1.csv')
    return feature_df
characterize(pd.read_csv('./train.csv'))