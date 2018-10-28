# -*- coding: utf-8 -*-
"""
Created on Sat May  5 10:53:26 2018

@author: lenovo
"""

import numpy as np
from scipy.optimize import leastsq



def fun(p,x):
    """定义想要拟合的函数"""
    k,b = p
    return k*x+b
def err(p,x,y):
    """定义误差函数"""
    return fun(p,x)-y

x = [1,2,3,4]
y = [6,5,7,10]

p0 = [1,1]
x1 = np.array(x)
y1 = np.array(y)
xishu = leastsq(err,p0,args=(x1,y1))
print(xishu[0])