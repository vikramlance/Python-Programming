'''
'''

#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

if (n%2 == 0) and  (m%2 ==0):
    k =  (int(n/2)) * (int(m/2)) 
if (n%2 == 0) and (m%2 !=0):
    k =  (int(n/2))* (int(m/2))+ (int(n/2)) 
if (n%2 != 0) and (m%2 ==0):
    k =  (int(n/2)) * (int(m/2)) + (int(m/2))
if (n%2 != 0) and (m%2 !=0):
    k =  (int(n/2))*(int(m/2)) + (int(n/2)) + (int(m/2)) + 1
print (int(k))