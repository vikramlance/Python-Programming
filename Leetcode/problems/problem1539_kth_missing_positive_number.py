"""
Input: arr = [2,3,4,7,11], k = 5
Output: 9

Input: arr = [1,2,3,4], k = 2
Output: 6
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        complete_range = len(arr) + k

        missing_values = []
        complete_arr = []
        for i in range(complete_range):
            complete_arr.append(i+1)

        x = 0
        for j in range(len(complete_arr)):
            if x < len(arr):
                if arr[x] != complete_arr[j]:
                   missing_values.append(complete_arr[j]) 
                else:
                    x +=1
            else:
                missing_values.append(complete_arr[j]) 
                x +=1
                
        return missing_values[k-1]
