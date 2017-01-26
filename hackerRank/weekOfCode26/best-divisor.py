'''
The probelem statement available in the pdf file - Best Divisor _ Week of Code 26 Question _ Contests _ HackerRank.pdf

problem statement:
https://www.hackerrank.com/contests/w26/challenges/best-divisor

input 

output
'''

import sys
import math

n = int(raw_input().strip())


def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

k= list(divisorGenerator(n))


    
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

best = 0
oldm=0
for i in k:
    m= sum_digits3(i)
    if m > oldm:
        best = i
        oldm= m
    if m == oldm and best > i:
        best = i
        oldm= m


print (best)
