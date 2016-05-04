#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    m = str(n)
    k=0
    for i in range(len(m)):
        if int(m[i]) != 0:
            if n%int(m[i]) ==0:
                k=k+1
    print k
        
    
