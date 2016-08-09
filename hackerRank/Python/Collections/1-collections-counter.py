'''
https://www.hackerrank.com/challenges/collections-counter
'''
from collections import Counter
a=raw_input()
b=Counter(map(int,raw_input().split()))
k=int(raw_input())
t=0
for i in range(k):
    s,p=raw_input().split()
    if int(s) in b.keys():
        t=t+int(p)
        b[int(s)]=b[int(s)]-1
        if b[int(s)]==0:
            del b[int(s)]
print t


