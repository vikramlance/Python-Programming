'''
Given an array Ai  and a number N, rotate the array left by N places.
'''

a=[4,99,12,3,0,77,134,985]
n=len(a)
k=3

a[::-1]
a[:n-k+1:-1]
a[n-k::-1]
print a


'''

rotating array right by n places

Rotate a one-dimensional array of n elements to the right by k steps. 
For instance, with n=7 and k=3, the array {a, b, c, d, e, f, g} is rotated to {e, f, g, a, b, c, d}.

def rotate(a,n):
	l=len(a)
	c=gcd(l,n)
	m=l/c
	step=l-n
	for i in range(c):
		 u=a[i]
		 idx=i
		 for j in range(1,m):
			 idx1=(idx+step)%l
			 a[idx]=a[idx1]
			 idx=idx1
		 a[idx]=u
	print a
rotate(a,n)
'''
