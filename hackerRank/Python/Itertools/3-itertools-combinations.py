'''

itertools.combinations(iterable, r) 
https://www.hackerrank.com/challenges/itertools-combinations

'''

from itertools import combinations

a=raw_input().split()
#b=sorted(list(combinations(a[0],int(a[1]))))
for i in range(1,int(a[1])+1):
    b=list(combinations(a[0],i))
    h=[]
    for j in b:
        h.append(sorted(j))
    for k in sorted(h):
        print ''.join(map(str, k))  

'''
Ideal answer

from itertools import combinations
S,k = raw_input().split()
for j in range(1,int(k)+1):
    for i in combinations(sorted(S),j):
        print "".join(i)

'''
