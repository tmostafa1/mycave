# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:44:25 2020

@author: tamanna
"""

#https://www.hackerrank.com/challenges/np-min-and-max/problem?h_r=next-challenge&h_v=zen
import numpy
line, row=input().split()
p=[]
for i in range(int(line)):
    p.append(list(map(int, input().split())))
my_arr=numpy.array(p)
a=numpy.min(my_arr, axis=1)
print(numpy.max(a))
    
