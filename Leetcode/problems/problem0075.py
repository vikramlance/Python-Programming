"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = {}
        
        for i in nums:            
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        
        index = 0
        keys = list(temp.keys())
        
        keys.sort()
        index = 0
        for j in keys:                                
            for k in range(temp[j]):
                nums[index] = j  
                index += 1
                
        return nums