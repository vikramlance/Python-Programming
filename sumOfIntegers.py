#!/bin/python

import sys

num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ',num_array



b=sum (num_array);
print (b);

def sumOfIntegers(num_array):
    total = 0
    for row in num_array:
        
        #print(row)
        total=total + row
        #print(total)
    return total
    
#print(total)
m=sumOfIntegers(num_array)
print("another way to calcualte sum using function")
print(m)
