'''
'''

import itertools
import re

m,n= (raw_input().strip().split())
matrix=[]
for _ in range(int(m)):
    matrix.append(list(raw_input().strip()))
#rotate matrix by 90 degree
arr = zip(*matrix[::-1])

def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr = list(reversed(zip(*arr[1:])))

spiralString= ''.join(list(itertools.chain(*transpose_and_yield_top(arr))))

#replace consecutive # in spiralString
newSpiralString= re.sub('#+','#',spiralString)

h= list(newSpiralString)

if h==['#']:
    print 0
    quit()
if h[0]=='#':
	
	if h[len(h)-1]=='#':
		print 1 + sum(1 for v in h[1:len(h)-1] if v=='#')
		quit()
	else:
		print 1 + sum(1 for v in h[1:len(h)] if v=='#')
		quit()
if h[len(h)-1]=='#' and h[0] !='#':
	print 1 + sum(1 for v in h[:len(h)-1] if v=='#')
	quit()

print 1 + sum(1 for v in h if v=='#')
