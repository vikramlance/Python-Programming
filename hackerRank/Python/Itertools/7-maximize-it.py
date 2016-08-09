'''
https://www.hackerrank.com/challenges/maximize-it
'''


from itertools import product

k,m=raw_input().split()

c=[]

for i in range(int(k)):
	b= map(int,(raw_input().split()))
	c.append(b[1:])
d=[]	
for i in list(product(*c)):
	d.append(   (sum(map(lambda x:x*x,i)))%int(m) )

print max(d)
