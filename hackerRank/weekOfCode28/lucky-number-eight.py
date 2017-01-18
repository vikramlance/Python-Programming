'''
Problem statement:
https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight

input 

output

'''


'''
All possible combinations of string are taken for following code. 


#!/bin/python

import sys
from itertools import combinations

n = int(raw_input().strip())
number = raw_input().strip()
# your code goes here
h=[]
g=[]
k = len(number)
for j in range(1,int(k)+1):
    b= list(combinations(number,j))
    for j in b:
        h.append(j)
    for k in (h):
        z = int(''.join(map(str, k)))
        g.append(z)
count=0


for m in set(g):
    if m%8==0 :
        count+=1
        
print ((count % ( (10**9) + 7 )) )
'''
