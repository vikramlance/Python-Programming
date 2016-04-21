#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
a=[]
for i in range (n-1,-1,-1):
    a.append(arr[i])
b=map(str,a)
print b
s=' '.join(b)
print s
    
