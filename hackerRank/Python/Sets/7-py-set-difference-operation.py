'''
https://www.hackerrank.com/challenges/py-set-intersection-operation
'''

a=raw_input()
b=set(map(int, raw_input().split()))
'''
print b 
print len(b)
'''

c=raw_input()
d=set(map(int, raw_input().split()))

print len(b.difference(d))
