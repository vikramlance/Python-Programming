from itertools import permutations

a=raw_input().split()
b=sorted(list(permutations(a[0],int(a[1]))))
for i in b:
       print ''.join(map(str, i))   
