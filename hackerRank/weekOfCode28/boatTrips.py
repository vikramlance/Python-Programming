'''

https://www.hackerrank.com/contests/w28/challenges/boat-trip
'''

#!/bin/python

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

for i in p:
    if i > c*m:
        print "No"
        quit()
print "Yes"
