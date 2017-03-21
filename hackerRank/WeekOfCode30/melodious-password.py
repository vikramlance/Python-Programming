'''


'''


import sys

import string

print string.ascii_lowercase


import itertools
# from itertools import

print '[a-z]'


#itertools.permutations(iterable[, r])



from itertools import permutations

#n = int(raw_input().strip())

'''
perms = [''.join(p) for p in itertools.permutations(iterable['stack', 2])]
print perms
'''

from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase,repeat = 2)]

print keywords
