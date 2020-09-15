"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

class solution():

    def contains_duplicate(self, arr):
        temp_set = set()
        for i in arr:
            if i in temp_set:
                return True
            else:
                temp_set.add(i)
        return False

arr = [1,1,1,3,3,4,3,2,4,2]
test = solution()

print (test.contains_duplicate(arr))



        
