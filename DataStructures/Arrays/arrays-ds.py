'''
Problem statement can be found at below location.
https://www.hackerrank.com/challenges/arrays-ds
'''


#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print ' '.join(map(str, arr[::-1]))
