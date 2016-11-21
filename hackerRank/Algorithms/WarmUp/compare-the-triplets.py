'''
https://www.hackerrank.com/challenges/compare-the-triplets
'''

#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a=[a0,a1,a2]
b=[b0,b1,b2]
alice=0
bob=0

for i in range(3):
    if a[i] > b[i]:
        alice+=1
    if a[i]<b[i]:
        bob+=1
print (str(alice)+' '+str(bob))
