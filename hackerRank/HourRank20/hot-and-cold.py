'''
https://www.hackerrank.com/contests/hourrank-20/challenges/hot-and-cold
'''


#!/bin/python

import sys

def isSatisfiable(c1, c2, h1, h2):
    # Complete this function

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = raw_input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)
