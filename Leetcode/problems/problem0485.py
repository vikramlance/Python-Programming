class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = curr_len = 0
        
        for num in nums:
            if num == 1:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
        max_len = max(max_len, curr_len)
        return max_len