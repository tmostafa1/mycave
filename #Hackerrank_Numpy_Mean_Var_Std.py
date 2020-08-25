# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:35:20 2020

@author: tamanna
"""
import numpy
number, length=input().split()
p=[]
for i in range(int(number)):
    p.append(list(map(int, input().split())))
my_arr=numpy.array(p)
print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
print(round(numpy.std(my_arr),11))
    
    