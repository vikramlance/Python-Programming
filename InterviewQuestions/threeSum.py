'''
http://www.byte-by-byte.com/threesum/
'''


a= [-1, 0, 1, 2, -1, -4]

print a
k = len(a)
b=[]

for i in range (k):
	for j in range(i+1,k):
		for m in range(j+1,k):
			if a[i] + a[j] + a[m] == 0:
				v=[a[i],a[j],a[m]]
				v.sort()
				if v not in b:
					b.append(v)

for i in b:
	print i
