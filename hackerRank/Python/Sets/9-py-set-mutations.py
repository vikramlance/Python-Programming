'''
https://www.hackerrank.com/challenges/py-set-mutations
'''

a=raw_input()


b=set(map(int, raw_input().split()))


N=int(raw_input().strip())

for N in range(0,N):
	c=raw_input().split()
	d=set(map(int, raw_input().split()))
	getattr(b, c[0])(d)	

print str(sum(b))
