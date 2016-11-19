'''

'''


import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
k=len(a)
a.sort()

if (a[1] - a[0]) >= (a[k-1] - a[k-2]):
    print  (a[k-1] - a[1])
else:
    print (a[k-2] - a[0])
