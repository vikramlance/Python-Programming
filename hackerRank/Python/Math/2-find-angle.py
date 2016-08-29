'''
https://www.hackerrank.com/challenges/find-angle
'''

import math
a=int(raw_input())
b=int(raw_input())


x= (math.sqrt(math.pow(a,2) + math.pow(b,2)))/2.0

y=math.acos(b/(2*x))

print str(int(round(math.degrees(y),0)))+ u'\N{DEGREE SIGN}'
