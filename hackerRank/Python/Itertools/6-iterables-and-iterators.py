
from itertools import combinations

a=raw_input()
b=list(raw_input().split())
k=int(raw_input())

count=0
counnt1=0
for j in combinations(b,k):
	counnt1=counnt1 + 1
	if 'a' in j:
		count = count +1

print float(count)/float(counnt1)
