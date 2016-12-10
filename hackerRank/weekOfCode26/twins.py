'''
Problem statement is available in pdf file - Twins _ Week of Code 26 Question _ Contests _ HackerRank.pdf
'''
import math
def prime(n):
    for i in range (2,int(n**0.5) + 1):
        if n%i==0:
            return "NO"
    return "YES"
