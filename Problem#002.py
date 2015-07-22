# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:12:38 2015

@author: Dell
"""
import time
#Fibonacci
#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.

#original solution
starttime = time.clock()
F_1 = 1
F_2 = 1
F = 0
sum = 0
while F_2 < 4000000:
    if F_2 % 2 == 0:
        sum += F_2
        print F_2
    F = F_1 + F_2
    F_1 = F_2
    F_2 = F
print sum
endtime = time.clock()
print('used time: %f s' %(endtime - starttime))

#1 1 2 3 5 8 13 21 34 55 89 144
#every third Fibonacci number is even
starttime = time.clock()
F_1 = 1
F_2 = 1
F = F_1 + F_2
sum = 0
while F < 4000000:
    sum += F
    print F    
    F_1 = F + F_2
    F_2 = F + F_1
    F = F_1 + F_2
print sum
endtime = time.clock()
print('used time: %f s' %(endtime - starttime))