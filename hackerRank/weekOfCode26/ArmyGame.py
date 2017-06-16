'''
problem statement can be found at below link. To understand the problem.
https://www.hackerrank.com/contests/w26/challenges/game-with-cells

also problem statement can be found in pdf file
- Army Game _ Week of Code 26 Question _ Contests _ HackerRank.pdf

add here

input 
2 2

output
1

'''
#!/bin/python3

import sys
#input

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

if (n%2 == 0) and  (m%2 ==0):
    k =  (int(n/2)) * (int(m/2)) 
if (n%2 == 0) and (m%2 !=0):
    k =  (int(n/2))* (int(m/2))+ (int(n/2)) 
if (n%2 != 0) and (m%2 ==0):
    k =  (int(n/2)) * (int(m/2)) + (int(m/2))
if (n%2 != 0) and (m%2 !=0):
    k =  (int(n/2))*(int(m/2)) + (int(n/2)) + (int(m/2)) + 1
print (int(k))
