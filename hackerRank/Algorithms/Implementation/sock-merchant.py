'''
https://www.hackerrank.com/challenges/sock-merchant

'''


import sys
import itertools


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

b = c.counter() 
