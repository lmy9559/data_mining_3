# -*- coding: utf-8 -*-

    
import matplotlib.pyplot as plt   
from os import listdir  
import numpy as np  
filename = './train.csv'
def file2matrix(filename,sex,age,fare):  
    fr = open(filename)  
    content = fr.readlines()
    content.remove(content[0])
    numberOfLines = len(content)         #get the number of lines in the file  
    returnMat = np.zeros((numberOfLines,3))        #prepare matrix to return  
    classLabelVector = []                       #prepare labels return     
    index = 0 #确保指针在最前面  
    
    for line in content:  
        line = line.strip()  
        listFromLine = line.split(',')  
        if listFromLine[sex]=='male':  
            listFromLine[sex]='0'  
        else:  
            listFromLine[sex]='1'  
        if listFromLine[age]=='':  
            listFromLine[age]=29.7   
        if listFromLine[fare]=='':  
            listFromLine[fare]=35.6   
                #年龄的缺省用平均年龄29.7代替         
        returnMat[index,:] = [listFromLine[sex],listFromLine[age],listFromLine[fare]]      #对应着性别，年龄和船票价  
        classLabelVector.append(int(listFromLine[1]))  
        index += 1  
    return returnMat,classLabelVector #return的位置一定要找对  
'''
dataset,classlabel=file2matrix('./train.csv',5,6,10)  
classlabel=np.array(classlabel)  
id0=np.where(classlabel==0)  
id1=np.where(classlabel==1)  
fig=plt.figure()    
ax=fig.add_subplot(111)   
p1=ax.scatter(dataset[id1,0],dataset[id1,1],color = 'r',label='1',s=20)  
p0=ax.scatter(dataset[id0,0],dataset[id0,1],color ='b',label='0',s=10)  
plt.legend(loc = 'upper right')  
plt.show   
'''

def autoNorm(dataSet):    
    minVals = dataSet.min(0)    
    maxVals = dataSet.max(0)    
    ranges = maxVals - minVals    
    normDataSet = np.zeros(np.shape(dataSet))#建立框架    
    m = dataSet.shape[0]#行数    
    normDataSet = dataSet - np.tile(minVals, (m,1))#每个数减该列最小    
    normDataSet = normDataSet/np.tile(ranges, (m,1))   #差再除以max-min    
    return normDataSet, ranges, minVals 

def classify0(inX, dataSet, labels, k):  
    dataSetSize = dataSet.shape[0]#4l  
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet#inx按4*1重复排列再与sataset做差  
    sqDiffMat = diffMat**2#每个元素平方  
    sqDistances = sqDiffMat.sum(axis=1)#一个框里的都加起来  
    distances = sqDistances**0.5#加起来之后每个开根号  
    sortedDistIndicies = distances.argsort() #返回的是数组值从小到大的索引值，最小为0  
    classCount={}            
    for i in range(k):#即0到k-1.最后得到的classCount是距离最近的k个点的类分布，即什么类出现几次如{'A': 1, 'B': 2}  
        voteIlabel = labels[sortedDistIndicies[i]]#返回从近到远第i个点所对应的类  
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1#字典模式，记录类对应出现次数.这里.get(a,b)就是寻找字典classcount的a对应的值，如果没找到a，就显示b  
    sortedClassCount = sorted(classCount.items(), reverse=True)  
    return sortedClassCount[0][0]  

def surviorclasstest():  
    hoRatio = 0.10      #hold out 10%  
    dataset,classlabel=file2matrix('train.csv',5,6,10)     #load data setfrom file  
    normMat, ranges, minVals = autoNorm(dataset)  
    m = normMat.shape[0]  
    numTestVecs = int(m*hoRatio)  
    errorCount = 0.0  
    for i in range(numTestVecs):  
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],classlabel[numTestVecs:m],10)  
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classlabel[i])  )
        if (classifierResult != classlabel[i]): errorCount += 1.0  
    print( "the total error rate is: %f" % (errorCount/float(numTestVecs))  )
    print( errorCount  )
    
def classifyperson():  
    dataset,classlabel=file2matrix('train.csv',5,6,10)  
    normMat, ranges, minVals = autoNorm(dataset)  
    testset,whatever=file2matrix('test.csv',4,5,9)  
    normMattest, rangestset, minValstest = autoNorm(testset)  
    h=testset.shape[0]  
    for i in range(h):  
        classifierResult = classify0(normMattest[i,:],normMat[:,:],classlabel[:],10)  
        print(classifierResult)

surviorclasstest()
#classifyperson()
