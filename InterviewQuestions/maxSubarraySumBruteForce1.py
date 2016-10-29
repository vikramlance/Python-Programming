a= [1,2,3,-3,7]

n=len(a)

if all(i<0 for i in a ):
	print max(a)
	print max(a)
	
	
elif all(i>=0 for i in a ):
	print sum(a)
	print a
	
else:
	newSum=0
	arr=[]
	for i in range(1,n+1):
		for j in range(n+1 -i):
			
			s=sum(a[j:j+i])
			
			if s> newSum:
				newSum=s
				arr=a[j:j+i]
				
	print newSum
	print arr
