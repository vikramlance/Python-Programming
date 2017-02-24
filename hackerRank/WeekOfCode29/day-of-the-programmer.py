'''
Problem can be found at below link 
https://www.hackerrank.com/contests/w29/challenges/day-of-the-programmer
'''

#!/bin/python

import sys


a = int(raw_input().strip())

if (2700 >= a >= 1919) :
  if a % 400 == 0:
    print "12.09." + str(a)
  elif a%4 ==0 and a%100 <> 0:
    print "12.09." + str(a)
  else:
    print "13.09." + str(a)
  
elif (1700 <= a <= 1917):
  if a%4 ==0:
    print "12.09." + str(a)
  else:
    print "13.09." + str(a)

elif (a == 1918):
  print "26.09." + str(a)
  
else:
  print 0
