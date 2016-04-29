#!/bin/python

import sys


n = int(raw_input().strip())

for i in range (0,n):
    print ' '*(n-1-i) + '#'*(i+1)
