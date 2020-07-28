


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = {}
        result = []
        for i in nums:
            if i not in temp:
                temp[i] = 1
            elif temp[i] == 1:
                temp[i] = 2
        for key in temp:
            if temp[key] == 1:
                result.append(key)
        
        return result
            
            
            
        