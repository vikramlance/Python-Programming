a=map (int, (raw_input().strip().split(' ')))
n=len(a)
def MS(k):
	best=cur=0
	for i in range(k):
		cur=max(cur+a[i], 0)
		best=max(best, cur)
	print best
MS(n)
