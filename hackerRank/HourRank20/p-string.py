'''
Problem statement link
https://www.hackerrank.com/contests/hourrank-20/challenges/p-string
'''


#!/bin/python

import sys

def countSubs(s):
    # Complete this function

# Return the number of non-empty perfect subsequences mod 1000000007
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = countSubs(s)
    print(result)

