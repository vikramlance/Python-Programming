'''
I am developing a solution for bin packing problem now need help in optimizing it. So the problem is as followed for example:
1. I have total 5738 lts of water need to be packed. 
2. I have 10 buckets sizes as followed: 700, 700, 1440, 1440, 2700, 2700, 2700, 2700, 2700, 2700

Now how i will select the buckets where my empty spaces will be lowest. My code is now able to select 2*2700 and one 700 bucket

'''
from itertools import combinations

amnt = 5738
clist = [700, 700, 1440, 1440, 2700, 2700, 2700, 2700, 2700, 2700]
mini=[]
m= amnt
for i in range (len(clist)):
	for j in combinations(clist,i):
		if (0 <= sum(j) - amnt <= m):
			m=sum(j) - amnt
			mini= j
print (mini)
