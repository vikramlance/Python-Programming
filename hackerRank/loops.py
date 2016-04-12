#!/bin/python

import sys


N = int(raw_input().strip())


for i in range (1,11):
    m=N*i
    print ("%d x %d = %d") %(N,i,m)
