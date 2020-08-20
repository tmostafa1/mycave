# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:47:36 2020

@author: tamanna
"""


#fromHackerrank_numpy.array
#https://www.hackerrank.com/challenges/np-arrays/problem
import numpy
def arrays(arr):
    n_arr=arr[::-1]
    a=numpy.array(n_arr, float)
    return a
arr = input().strip().split(' ')
result = arrays(arr)
print(result)