'''

'''


#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    h=1
    for i in range (n):
        if i%2 ==0:
            h=h+h

        else:
            h=h+1

    print h
