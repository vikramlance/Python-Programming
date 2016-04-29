#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
p=0
m=0
z=0
for i in arr:
    if i > 0:
        p=p+1
    elif i < 0:
        m=m+1
    else:
        z=z+1
#print p 
#print n
print (p/float (n))
print (m/float (n))
print (z/float (n))
