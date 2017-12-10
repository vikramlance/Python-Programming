"""
http://www.geeksforgeeks.org/yatra-com-interview-experience-set-10/

Given an array, find triplets whose sum equals the given number. 
For Example –
Find if there exists 3 numbers in the given array whose sum equals the given sum.
Array =  {2, 7, 4, -1, 3}  and sum = 6.

Output :   4, -1, 3  
Since 4 + (-1) + 3 = 6

Improved time complexity
"""

array =  [2, 7, 4, -1, 3]
number_sum = 6

array_len = len(array)

for item in xrange(array_len - 2):
    a = array[item]
    b = array[item + 1]
    c = number_sum - a - b 
    if c in array[item + 2 : array_len]:
            print(a,b,c)
