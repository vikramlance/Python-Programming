'''
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
'''

import cmath
a,b=raw_input().split()
x,y=raw_input().split()


c=complex(float(a),float(b))
d=complex(float(x),float(y))



print (c+d)
print (c-d)
print (c*d)
print (c/d)
print (abs(c))
print (abs(d))
