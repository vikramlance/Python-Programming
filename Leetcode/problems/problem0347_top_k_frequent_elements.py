"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

"""
from collections import deque
class solution:

    def top_k_frequent(self, nums, k):
        frequency_dict = {}

        for i in range(len(nums)):

            if nums[i] in frequency_dict:
                frequency_dict[nums[i]] = frequency_dict[nums[i]] + 1
            else:
                frequency_dict[nums[i]] = 1

        print(frequency_dict)
        frequency_list = deque()
        for key in frequency_dict:
            frequency_list.append(frequency_dict[key])

        sorted_frequncy_list = sorted(frequency_list)

        # find the top k'th element
        top_k_th_element = sorted_frequncy_list[len(sorted_frequncy_list) - k]

        top_k_frequent_list = deque()
        for j in frequency_dict:
            if frequency_dict[j] >= top_k_th_element:
                top_k_frequent_list.append(j)

        return list(top_k_frequent_list)


nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1,2]
test = solution()

print(test.top_k_frequent(nums, k))
