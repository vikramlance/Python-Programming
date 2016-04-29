#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
#print a
d1=0
d2=0
for i in range(0,n):
    #print i
    d1+= a[i][i]
#print d1        
'''
        print j
        if i==j:
            print a[i][j]
            d1+= a[i][j]
'''
#print "value of n"
#print n
for k in range(n-1,-1,-1):
    #print "in loop"
    #print k
    for l in range(0,n):
        #print l
        if (k+l)==(n-1):
            #print "k l"

            #print a[k][l]
            d2+=a[k][l]
#print d2
print abs(d1-d2)
        
    



    
    
