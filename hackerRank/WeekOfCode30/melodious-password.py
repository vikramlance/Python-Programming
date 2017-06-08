'''
Problem statement 
https://www.hackerrank.com/contests/w30/challenges/melodious-password

'''

import string
print string.ascii_lowercase


import itertools
# from itertools import
#itertools.permutations(iterable[, r])
from itertools import permutations
consonant = 'bcdfghjklmnpqrstvwxz'
vowel ='aeiou' 
#n = int(raw_input().strip())

for i in consonant:
  print i
'''
combo_list = [''.join(p) for p in itertools.permutations(iterable['stack', 2])]
print combo_list
'''

from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase,repeat = 2)]

#print keywords

