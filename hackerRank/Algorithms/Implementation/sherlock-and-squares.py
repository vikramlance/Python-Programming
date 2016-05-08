#!/bin/python

from math import *
 
if __name__ == '__main__':
    t = input()
    for a in range(t):
        n, k = map(int, raw_input().split())
        n = ceil(sqrt(n))
        k = floor(sqrt(k))
        print int(k - n) + 1








'''
import math
import itertools
t=int(raw_input().strip())

for a in range(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    m=0
    #itertools.count(start=0, step=1)
    for i in itertools.count(start=n, step=1):

        if (math.sqrt(i).is_integer()):
            m=m+1
        if i == k:
            print m
            break

'''  
