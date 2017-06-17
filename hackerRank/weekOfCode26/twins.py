'''
Problem statement is available in pdf file - Twins _ Week of Code 26 Question _ Contests _ HackerRank.pdf

Problem statement:
https://www.hackerrank.com/contests/w26/challenges/twins
----
add your code here 
input format
9234567 9876543


3875185 4608449
----
output format
3334
4161



** for some test cases below code will not pass the time limit test and gets timed out on few of the hackerrank test cases

'''


import math

n,m = raw_input().split()
n=int(n)
m=int(m)
primes = []
def prime(n):
    
    if n in primes:
        return "YES"        
    for i in range (2,int(n**0.5) + 1):
        if n%i==0:
            return "NO"
    if n==1:
        return "NO"
    primes.append(n)
    return "YES"
count=0
if n%2==0:
    n=n+1
    
if n>=5:
    for i in range(n,m-1,2):
        if (i + 1)%6== 0:
            if prime(i)=='YES' and prime(i+2)=='YES':
                count+=1
else:
    for i in range(n,m-1,2):
        if prime(i)=='YES' and prime(i+2)=='YES':
            count+=1
print count


