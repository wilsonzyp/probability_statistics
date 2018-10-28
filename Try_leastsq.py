# -*- coding: utf-8 -*-
"""
Created on Sat May  5 10:25:48 2018

@author: lenovo
"""
import matplotlib.pyplot as plt

def leastsq(x,y):
    """x/y分别为要拟合的数据"""
    meanx = sum(x)/len(x)
    meany = sum(y)/len(y)
    xsum = 0.0
    ysum = 0.0
    
    for i in range(len(x)):
        xsum +=(x[i]-meanx)*(y[i]-meany)
        ysum +=(x[i]-meanx)**2
        
    k = xsum/ysum
    b = meany - k*meanx
    
    return k,b

x = [1,2,3,4]
y = [6,5,7,10]

k,b = leastsq(x,y)
# print(k,b)
xx = [0,6]
yy = []
for xi in xx:
    yy.append(k*xi+b)
    
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.plot(xx,yy)
plt.scatter(x,y,s=50,c='r')
plt.title('最小二乘法')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.axis([xx[0],xx[-1],0,yy[-1]])
plt.show()