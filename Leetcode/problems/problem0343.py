"""



343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.



--------- wrong answer 

class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        max_prod = {}
        
        for i in range(2, n+1):
            if i % 2 == 0:
                
                max_prod[i] = []
                
                mid = int(i/2)
                
                if mid > 3:
                    max_prod[i].extend(list(x**2 for x in max_prod[mid]))
                else:
                    max_prod[i].extend([mid**2])
                    
                
            else:
                max_prod[i] = []
                
                mid = math.floor((i+1)/2)
                
                if mid > 3:
                    max_prod[i].extend(max_prod[mid])
                else:
                    max_prod[i].extend([mid])
                    
                if mid-1 > 3:
                    max_prod[i].extend(max_prod[mid-1])
                else:
                    max_prod[i].extend([mid-1])
                    
        result = 0
        
        for j in max_prod[n]:
            if result:
                result = result*j
            else:
                result = j
        return result

"""


class Solution:
    def integerBreak(self, n: int) -> int:        
        
        result = 1

        base_cases = {2: 1, 3:2}

        if n < 4:
            return base_cases[n]
        
        while n > 4:          
            result *= 3
            n -= 3

        return result*n
                                    
test = Solution()

print(test.integerBreak(10))                