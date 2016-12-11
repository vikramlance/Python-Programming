'''
Problem statement is available in pdf file - Twins _ Week of Code 26 Question _ Contests _ HackerRank.pdf
'''

import math

n,m = raw_input().split()
n=int(n)
m=int(m)
def prime(n):
    for i in range (2,int(n**0.5) + 1):
        if n%i==0:
            return "NO"
    return "YES"
count=0
for i in range(n,m-1):
    if prime(i)=='YES' and prime(i+2)=='YES':
        count+=1
print count
