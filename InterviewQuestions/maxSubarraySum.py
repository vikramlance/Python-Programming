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
	flag=0
	for i in range(n):
		max_ending_here = max_ending_here+a[i] 
		if max_ending_here<0:
			max_ending_here=0
		if max_so_far< max_ending_here:
			max_so_far=max_ending_here
	print max_so_far
