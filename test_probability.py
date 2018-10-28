# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:21:18 2018

@author: lenovo
"""

import random
import numpy

# ans = [random.choice(['A','B','C','D']) for i in range(10)]
# print(ans)
answer = []
interval = []
lasti = 0
count = 0
for i in range(1000):
    j = random.randint(0,9)
    if j == 0:
        answer.append('*')
        if lasti > 0:
            interval.append(i-lasti-1)
        lasti = i
        count+=1
    else:
        answer.append('-')
print('accident probability: '+str(count/len(answer)*100)+'%')
print('accident times: '+str(count))

statics = numpy.zeros(9)
tale = []
for i in interval:
    if i>35:
        statics[0]+=1
    elif 30<i<=35: 
        statics[1]+=1
    elif 25<i<=30:
        statics[2]+=1
    elif 20<i<=25:
        statics[3]+=1
    elif 15<i<=20:
        statics[4]+=1
    elif 10<i<=15:
        statics[5]+=1
    elif 5<i<=10:
        statics[6]+=1
    elif 0<i<=5:
        statics[7]+=1
    elif i==0:
        statics[8]+=1
tale=['    i>35 | ','30<i<=35 | ','25<i<=30 | ','20<i<=25 | ','15<i<=20 | ','10<i<=15 | ',' 5<i<=10 | ','  0<i<=5 | ','    i==0 | ']
for i in range(len(tale)):
    tale[i]+='发生次数：'+str(int(statics[i]))
    tale[i]+=' 发生概率：'+str(int(statics[i]/count*1000)/10)+'%'
    print(tale[i])
    
    

#print(answer)