"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        item_dict = {}
        result = []
        for i in nums:
            if i in item_dict:
                item_dict[i] += 1
            else:
                item_dict[i] = 1
        for j in item_dict:
            if item_dict[j] > 1:
                result.append(j)
        return result
