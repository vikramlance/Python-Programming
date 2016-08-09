'''
https://www.hackerrank.com/challenges/defaultdict-tutorial
'''


from collections import defaultdict

n,m=raw_input().split()

d = defaultdict(list)

for i in range(int(n)):
    d['A'].append(raw_input())
for j in range(int(m)):
    d['B'].append(raw_input())    
for k in d['B']:
    indices = [i+1 for i, x in enumerate(d['A']) if x == k]
    if indices == []:
        print -1
    else:
        print ' '.join(map(str,indices))
