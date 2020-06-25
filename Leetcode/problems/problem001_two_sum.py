class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

            if target - nums[i] in nums[i + 1:] and i != nums.index(target - nums[i]):
                return [i, nums.index(target - nums[i])]


test_two_sum = Solution()

result = test_two_sum.two_sum([1, 2, 7, 9, 4, 3], 12)

print(result)
