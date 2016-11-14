'''

'''


#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
v=[a,b,c,d,e]
v.sort()

mini= sum(v[:4]) 
maxi= sum(v[1:])

print (str(mini)+" "+str(maxi) )
