# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:34:11 2020

@author: tamanna
"""
import numpy
a,b=input().split()
p=[]
for i in range(int(a)):
    p.append(list(map(int, input().split())))
my_arr=numpy.array(p)
e=numpy.sum(p, axis=0)
print(numpy.prod(e))
    