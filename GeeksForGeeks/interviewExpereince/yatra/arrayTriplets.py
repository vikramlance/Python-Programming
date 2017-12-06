"""
http://www.geeksforgeeks.org/yatra-com-interview-experience-set-10/

Given an array, find triplets whose sum equals the given number. 
For Example –
Find if there exists 3 numbers in the given array whose sum equals the given sum.
Array =  {2, 7, 4, -1, 3}  and sum = 6.

Output :   4, -1, 3  
Since 4 + (-1) + 3 = 6

"""
import itertools

array =  [2, 7, 4, -1, 3]
number_sum = 6

combos = itertools.combinations(array, 3)

combo_list = list(combos)

for item in combo_list:

    if sum(item) == number_sum:
        print(item)
