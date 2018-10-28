# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:22:31 2018

@author: lenovo
"""

import numpy as np 
import matplotlib.pyplot as plt
import math

u = 0 # 均值为0
#u01 = -2
sig = 4#math.sqrt(10)  # 标准差δ

x = np.linspace(u-1*sig,u+1*sig,50)

y_sig = np.exp(-(x-u)**2/(2*sig**2))/(math.sqrt(2*math.pi)*sig)

print('max y_sig:'+str(np.max((y_sig))))

plt.plot(x,y_sig,'r-',linewidth = 2)
plt.grid(True)
plt.show()