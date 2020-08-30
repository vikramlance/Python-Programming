class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        in +ve int arr,  find a pattern of length m that is repeated k or more times.
         arr = [1,2,4,4,4,4], m = 1, k = 3
         arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
         arr = [1,2,3,1,2], m = 2, k = 2 false - not consecutive
         arr = [2,2,2,2], m = 2, k = 3 false - only 2 times .. not 3 
         
         arr = [2,2] m = 1, k = 2
         
         first find the pattern of length m
         then check if its repeated k times?
        
        length m - slding window - check window of len m and then move the window -- keep the count of repeatition
        """
        len_arr = len(arr) 
        # 4
        count = 0
        # 0
        for i in range(len_arr - m +1): 
            # 0 1 
            pattern = arr[i:i+m] 
            # 1 
            count = 1
            
            for j in range(i+m, len_arr - m+1, m):
                # 
                if arr[j: j+m] == pattern:
                    count +=1
                else:
                    break
                if count == k:
                    return True
        return False
