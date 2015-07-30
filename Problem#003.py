# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:17:18 2015

@author: Dell
"""
#largest prime factor

import time

def factor(n):
    i = 2
    factors = []
    while n >= i:
        if n % i == 0:
            factors.append(i)        
            n /= i
            #i = 2
        else:
            i += 1
    return factors
                
starttime = time.clock()

print factor(600851475143)

endtime = time.clock()

print('used time: %f s' %(endtime - starttime))