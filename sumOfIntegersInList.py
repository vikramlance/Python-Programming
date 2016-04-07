#sum of integer
#!/bin/python

import sys
import os

# Complete the function below.


def  sumOfIntegers(arr):
    total =0
    for row in arr:
        total=total + row
    return total

#f = open(os.environ['OUTPUT_PATH'], 'w')
    

_arr_cnt = 0
print("Enter number of elements in the list")
_arr_cnt = int(raw_input())
_arr_i=0
_arr = []
print("Enter elements in the list")
while _arr_i < _arr_cnt:
    _arr_item = int(raw_input());
    _arr.append(_arr_item)
    _arr_i+=1
    
print("Sum of elements in the list")
res = sumOfIntegers(_arr)
print(res)

#f.write(str(res) + "\n")

#f.close()
