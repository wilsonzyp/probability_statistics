# -*- coding: utf-8 -*-
"""
Created on Sat May  5 11:06:56 2018

@author: lenovo
"""

 # -*- coding: utf-8 -*-

import numpy as np  

import matplotlib.pylab as plt  

from scipy import stats  

x =[3.5, 2.5, 4.0, 3.8, 2.8, 1.9, 3.2, 3.7, 2.7, 3.3]   #高中平均成绩  

y =[3.3, 2.2, 3.5, 2.7, 3.5, 2.0, 3.1, 3.4, 1.9, 3.7]   #大学平均成绩  

  #linregress(x,y)线性回归函数

slope, intercept, r_value, p_value, std_err =stats.linregress(x,y)  

'''

  Out[37]: LinregressResult(slope=0.70389344262295073, intercept=0.71977459016393475, 

  rvalue=0.68345387256609358, pvalue=0.029341978126562161, stderr=0.26581031503816904)

'''

slope =round(slope,3)  #保留三位小数
intercept =round(intercept,3)  
print(slope, intercept)  

  #绘图用

def f(x, a, b):  
    return a +b*x  

xdata =np.linspace(1, 5, 20)  

plt.grid(True)  
plt.xlabel('x axis')    
plt.ylabel('y axis')   
plt.text(2.5, 4.0, r'$y = '+str(intercept) +' + '+str(slope) +'*x$', fontsize=18)  
plt.plot(xdata, f(xdata, intercept,slope), 'b', linewidth=1)  
plt.plot(x,y,'ro')  
plt.show()  

