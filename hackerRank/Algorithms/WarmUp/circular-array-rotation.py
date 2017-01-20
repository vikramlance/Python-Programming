'''
need to modify for k > n
'''

#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

new = a[:(n-k)][::-1]
new1= a[(n-k):][::-1]
h = new + new1
final =  h[::-1]
for a0 in xrange(q):
    m = int(raw_input().strip())
    print final[m]
