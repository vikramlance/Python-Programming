'''
shuffle array randomly
'''

import random

m=range(1,20,2)
print m
p=[]
for i in range(10):
	k=random.randint(0, 9-i)
	print k
	p.append(m[k])
	m.pop(k)

print p
