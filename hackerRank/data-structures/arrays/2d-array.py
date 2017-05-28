'''
https://www.hackerrank.com/challenges/2d-array

'''

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
print arr
sum =0
for i in range(4):
  for j in range (i,i+3):
    sum= sum + arr[i][j]
    print sum
