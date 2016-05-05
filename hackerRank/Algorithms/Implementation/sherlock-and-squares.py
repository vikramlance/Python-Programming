#!/bin/python
import math
t=int(raw_input().strip())

for a in range(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    m=0
    for i in xrange(n,k+1):
        if (math.sqrt(i).is_integer()):
            m=m+1
    print m
