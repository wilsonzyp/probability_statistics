# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:11:17 2018

@author: lenovo
"""

import numpy
# 假设有5000个学生，他们的身高和体重分别符合:
# X~N(1.75,0.2)
# Y~N(100,10)
# 的正态分布
x = numpy.round(numpy.random.normal(1.75,0.2,5000),2)
y = numpy.round(numpy.random.normal(100,10,5000),2)

z = numpy.column_stack((x,y))
print(z)

# 输出身高均值
print(numpy.mean(z[:,0]))
# 输出身高中位数
print(numpy.median(z[:,0]))
# 输出两组数据相关系数
print(numpy.corrcoef(z[:,0],z[:,1]))
# 输出身高标准差
print(numpy.std(z[:,0]))