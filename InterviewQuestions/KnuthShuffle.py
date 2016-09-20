import random

i=range(1,20,2)
print i

for a in range(10):
	b=random.randint(0, 9)
	i[b], i[a] = i[a], i[b]


print i
