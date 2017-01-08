'''
Problem statement:
https://www.hackerrank.com/contests/hourrank-16/challenges/leonardo-and-lucky-numbers

input 
4
1
4
11
17

output
No
Yes
Yes
No

'''

#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    n = long(raw_input().strip())
    if n%7==0 or n%4==0 or n%11==0  or (n%11)%7==0 or (n%11)%4==0 or n>17:
        #or n%7==4 or n%4==3
        print ("Yes")
    else:
        print ("No")
