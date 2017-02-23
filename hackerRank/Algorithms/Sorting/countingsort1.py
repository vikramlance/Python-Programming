'''

https://www.hackerrank.com/challenges/countingsort1

'''

from collections import Counter

a= raw_input()
b= map(int, raw_input().split())

p = []
for i in range(100):
    if i in b:
      p.append(b.count(i))
    else:
      p.append(0)
print ' '.join(map(str, p))
