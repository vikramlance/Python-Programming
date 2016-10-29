'''
Kadane's algorithm
'''


a=map (int, (raw_input().strip().split(' ')))
n=len(a)

p=sum(1 for number in a if number < 0)

if p==n:
	print max(a)
else:
	max_so_far=0
	max_ending_here=0
	for i in range(n):
		max_ending_here = max_ending_here+a[i] 
		if max_ending_here<0:
			max_ending_here=0
		if max_so_far< max_ending_here:
			max_so_far=max_ending_here
	print max_so_far
	
'''
a= [1,2,3,-3,7] 

#[1,2,-3,2,3,4,-1,4,6]

print sum(a[1:2])

print all(i >= 30 for i in a)

n=len(a)

maxSo=0
maxH=0
arr=[]
for i in range (n):
	
	maxH= maxH+ a[i]
	
	if maxH < 0:
		maxH=0
		arr=[]
	else:
		arr.append(a[i])
		
	if maxH > maxSo:
		maxSo = maxH
		
print maxSo
print arr
'''
