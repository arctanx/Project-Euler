# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:20:49 2015

@author: Dell
"""

import time

def palindromic():
    ans = 0
    for i in range(10, 1000):
        for j in range(10, 1000):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > ans:
                ans = k
    return ans
    
starttime = time.clock()

print palindromic()

endtime = time.clock()

print('used time: %f s' %(endtime - starttime))