# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:03:35 2015

@author: Dell
"""
import time

#original thought
starttime = time.clock()
n = 1000
sum = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum
endtime = time.clock()
print 'used time: %f s' %(endtime - starttime)

#new version after reading 001_overview.pdf
starttime = time.clock()
target = 999
tmp = 0
def SumDivisibleBy(x):
    tmp = target // x
    return x*tmp*(tmp+1)/2
print SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)
endtime = time.clock()
print 'used time: %f s' %(endtime - starttime)
