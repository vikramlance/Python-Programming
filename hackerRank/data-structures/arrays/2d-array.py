'''
https://www.hackerrank.com/challenges/2d-array

'''

#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
# print arr
# counter=0
sum_new=0
sum_old=0
for i in range(4):
  for j in range (4):
    sum=0
    for k in range (i,i+3):
      for l in range (j,j+3):
        # print ("k is %d" %(k)) 
        # print ("l is %d" %(l))
        # print arr[k][l]
        if (k == i+1 and l == j ) or (k==i+1 and l==j+2):
          # print "not sum"
          pass
        else:
          sum=sum+arr[k][l]
    
    sum_new= sum
    if sum_new > sum_old :
      sum_old = sum_new
    # print "sum is %d" %(sum)
    # counter = counter+1
    
print sum_old  
# print counter   
