"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        rem = num % 4 # 0
        div = num // 4 # -16
        count = 1
        
        if num < 0:
            while div <= -4 and rem == 0:
                rem = div % 4  # 0
                div = div // 4 # -1
                if rem != 0:
                    return False
                count += 1
        else:            
            while div >= 4 and rem == 0:
                rem = div % 4 
                div = div // 4
                if rem != 0:
                    return False
        
        print(div, rem, count)
            
        if div == 1 and rem == 0:
            return True
        elif div == -1 and rem ==0 and count % 2 == 1:
            return True                
        else:
            False

test = Solution()
print(test.isPowerOfFour(-64))
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        rem = num % 4 # 0
        div = num // 4 # -16
        
        if num < 0:
            return False
        elif num == 1:
            return True
        else:            
            while div >= 4 and rem == 0:
                rem = div % 4 
                div = div // 4
                if rem != 0:
                    return False
    
            
        if div == 1 and rem == 0:
            return True              
        else:
            False