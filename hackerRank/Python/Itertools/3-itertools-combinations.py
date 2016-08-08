from itertools import combinations

a=raw_input().split()
#b=sorted(list(combinations(a[0],int(a[1]))))
for i in range(1,int(a[1])+1):
    b=sorted(list(combinations(a[0],i)))
    h=[]
    for j in b:
        h.append(sorted(j))
    for k in sorted(h):
        print ''.join(map(str, k))  
