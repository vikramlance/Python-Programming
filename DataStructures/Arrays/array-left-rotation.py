'''
https://www.hackerrank.com/challenges/array-left-rotation

python 3
'''

n, d = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

d %= n
print(*(arr[d:] + arr[:d]))
