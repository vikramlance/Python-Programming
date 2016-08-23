'''
https://www.hackerrank.com/challenges/py-collections-deque
'''


from collections import deque
n=int(input())
d = deque()
for _ in range(n):
    command, *args = input().split()
    getattr(d, command)(*args)
print (' '.join(map(str,(d))))
