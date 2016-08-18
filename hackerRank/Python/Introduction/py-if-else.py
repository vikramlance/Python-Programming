'''
https://www.hackerrank.com/challenges/py-if-else
'''

#!/bin/python

import sys


N = int(raw_input().strip())

print((lambda n:'Weird' if n % 2 or 5 < n < 21 else 'Not Weird')(N))
