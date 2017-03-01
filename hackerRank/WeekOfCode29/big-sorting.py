'''
Problem statement can be found at below link 
https://www.hackerrank.com/contests/w29/challenges/big-sorting
'''

import sys
#read the input 
n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here


b = (map(int,unsorted))
b.sort()

for j in b:
    print j
