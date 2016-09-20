import random

i=range(1,3)
print i

j=len(i)
print j
if j < 2:
	print i
else:
	for a in range(j):
		b=random.randint(0,j-a)
		i[b], i[a] = i[a], i[b]
	print i
