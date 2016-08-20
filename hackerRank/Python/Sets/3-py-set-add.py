'''
https://www.hackerrank.com/challenges/py-set-add
'''

a=int(raw_input().strip())
b=set()
for i in range(a):
    b.add(raw_input().strip())
print len(b)
