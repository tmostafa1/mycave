# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:52:07 2020

@author: tamanna
"""

#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import numpy
r, c= input().split()
b=[]
for i in range(int(r)):
    p=list(map(int, input().split()))
    b.append(p)
my_array=numpy.array(b)
print(numpy.transpose(my_array))
print(my_array.flatten())
    