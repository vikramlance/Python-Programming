'''
maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array of numbers which has the 
largest sum. For example, for the sequence of values −2, 1, −3, 4, −1, 2, 1, −5, 4; the contiguous subarray with the largest sum 
is 4, −1, 2, 1, with sum 6.
'''

# brute force method 


a= map (int, (raw_input().strip().split(' ')))
print a
# 1,6,11,16
k=len(a)
m=a

s=0
s_old=0
s_max=[]
for i in range(k):
	# 0 1 2 3
	for j in range(i,k+1):
		s=sum(m[i:j])
		#print m[i:j]
		if s> s_old:
			s_old=s
			s_max=m[i:j]
			#print s_max

print s_max
