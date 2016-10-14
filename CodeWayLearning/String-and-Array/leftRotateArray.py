'''
Given an array Ai  and a number N, rotate the array left by N places.
'''

a=[4,99,12,3,0,77,134,985]
n=len(a)
k=3

a[::-1]
a[:n-k+1:-1]
a[n-k::-1]
print a
