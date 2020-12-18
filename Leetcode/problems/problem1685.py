"""



class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        result = []
        len_nums = len(nums)
        for i in range(len_nums):
            abs_sum = 0
            for j in range(len_nums):
                abs_sum += abs(nums[i] - nums[j])
            result.append(abs_sum)
                
        
        return result


class Solution:
    def getSumAbsoluteDifferences(self, nums):
        
        result = []        
        len_nums = len(nums)
        temp = {}
        for i in range(1, len_nums):
            temp[i] = abs(nums[i] - nums[i-1])
            
        
        for j in range(len_nums):
            abs_sum = 0 
            x = j 
            while x > 0:
                abs_sum += x*temp[x]
                x -= 1

            y = j + 1

            while y <= len_nums -1:
                abs_sum += (len_nums - y )*temp[y]
                y += 1

            result.append(abs_sum)
        
        return result


Input: nums = [2,3,5]
Output: [4,3,5]

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

1 4  3 3

1 4 6 



temp = {
    1: 3,
    2: 2,
    3: 2,
    4: 2
}
j = 3 

3* 2 + 2* 2 + 1* 3 

len -1 - curr index 

"""
class Solution:
    def getSumAbsoluteDifferences(self, nums):
        
        result = []        
        len_nums = len(nums)
        temp = {}
        for i in range(1, len_nums):
            temp[i] = abs(nums[i] - nums[i-1])
            
        
        for j in range(len_nums):
            abs_sum = 0 
            x = j 
            while x > 0:
                abs_sum += x*temp[x]
                x -= 1

            y = j + 1

            while y <= len_nums -1:
                abs_sum += (len_nums - y )*temp[y]
                y += 1

            result.append(abs_sum)
        
        return result
        
        
        