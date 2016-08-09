'''
itertools.combinations_with_replacement(iterable, r) 
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

'''

from itertools import combinations_with_replacement


s,k = raw_input().split()

for i in list(combinations_with_replacement(sorted(s),int(k))):
    print ''.join(map(str,i))
