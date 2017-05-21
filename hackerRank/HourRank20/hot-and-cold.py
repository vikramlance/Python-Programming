'''
https://www.hackerrank.com/contests/hourrank-20/challenges/hot-and-cold
'''


#!/bin/python

import sys

def isSatisfiable(c1, c2, h1, h2):
    if c1<=c2 :
        lower = c2
    else:
        lower=c1
    if h1<=h2:
        higher = h1
    else:
        higher= h2
    if lower<=higher:
        return "YES"
    else:
        return "NO"
    # Complete this function

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = raw_input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)

