'''
https://www.hackerrank.com/challenges/sock-merchant

'''


#!/bin/python

import sys
import collections


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
count=0
counter=collections.Counter(c)
for i in counter.values():
    count+=i/2
print count
