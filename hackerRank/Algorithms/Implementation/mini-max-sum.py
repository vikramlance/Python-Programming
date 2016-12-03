#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

k= [a,b,c,d,e]

k= sorted(k)

if k[1] - k[0] > k[4] -k[3]:
    max= sum(k) - k[0]
    min = sum(k) - k[4]
else:
    min= sum(k) - k[4]
    max = sum(k) - k[0]    
print (str(min)+' '+ str(max))
