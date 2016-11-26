'''
https://www.hackerrank.com/challenges/angry-professor
'''

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    p=0
    q=0
    for i in range(0,n):
    	if a[i]>0:
    		p=p+1
    	else:
    		q=q+1
    if q>=k:
    	print 'NO'
    else:
    	print 'YES'
