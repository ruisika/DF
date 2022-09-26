# -*- coding:utf-8 -*-
import numpy as np
from nltk.probability import FreqDist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import model_selection
import re

from config import ML_file, ML_file1,ML_id

#测试样本数
N=150

#获取用户的样本命令总计
def load_user_cmd_new(filename):
    cmd_list=[]
    dist=[]
    with open(filename) as f:
        i=0
        x=[]
        for line in f:
            line=line.strip('\n')
            x.append(line)
            dist.append(line)
            i+=1
            if i == 100:
                cmd_list.append(x)
                x=[]
                i=0
 
    fdist = list(FreqDist(dist).keys())
    return cmd_list,fdist

#提取特征值
def get_user_cmd_feature_new(user_cmd_list,dist):
    user_cmd_feature=[]
 
    for cmd_list in user_cmd_list:
        v=[0]*len(dist)
        for i in range(0,len(dist)):
            if dist[i] in cmd_list:
                v[i]+=1
                #print(i,dist[i], v[i])
        user_cmd_feature.append(v)
    #print(user_cmd_feature)
    return user_cmd_feature
 
#目标值
def get_label(filename,index=0):
    x=[]
    with open(filename) as f:
        for line in f:
            line=line.strip('\n')
            x.append(int(line.split()[index]))
    return x

#获取用户历史命令
def load_user_history(dir,s_n,e_n):
    x = []
    if(s_n<e_n):
        print('输入有误')
        exit()
    with open(dir,'r',encoding='utf-8') as f:
        data = f.read()
        data1 = re.split('\n',data)
        data2 = data1[::2]
        if(e_n==''):
            data3 = data2[int(s_n):]
        else:
            data3 = data2[int(s_n):int(e_n)]
    data4 = []
    for i in range(len(data3)):
        a = re.split(' ',data3[i])
        data4.append(a[0])
    return data4

def a():
    user_cmd_list,dist=load_user_cmd_new(ML_file)
    user_cmd_feature=get_user_cmd_feature_new(user_cmd_list,dist)

    labels=get_label(ML_file1,ML_id)
    y=[0]*50+labels
 
    x_train=user_cmd_feature[0:N]
    y_train=y[0:N]
 
    x_test=user_cmd_feature[N:150]
    y_test=y[N:150]

    user_history = load_user_history(input('用户命令目录位置'),input("开始行数（如果为负数则为倒数第多少行）"),input('结束行数(结束行值如果为-1则匹配最后)'))

    ceshi = get_user_cmd_feature_new(user_history,dist)


    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(x_train, y_train)
    y_predict=neigh.predict(ceshi)
    n = 0 
    for i in range(len(y_predict)):
        if(y_predict[i]==1):
            n+=1
    print('共有'+str(n)+"命令异常,占比"+str(n/len(y_predict)))
    with open("/bishe/mlhist.txt",'a') as f:
        f.write('共有'+str(n)+"命令异常,占比"+str(n/len(y_predict)))

