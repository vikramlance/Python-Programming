'''
Below program reverses the array by using temporary variable.
'''

a=[1,2,3,4]

n=len(a)

for i in range(n/2):
	temp=a[i]
	a[i]=a[n-i-1]
	a[n-i-1]= temp
print a
