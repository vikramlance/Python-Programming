"""


# below solution works but times out/ goes out of given memory
from itertools import permutations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        temp_list = []
        temp_str = ''
        for i in range(n):
            temp_str = temp_str + '()'
            
        # find all permutation of temp_str 
        # print("aaa", temp_str)
        perms = [''.join(p) for p in permutations(temp_str)]
        
        # print(perms)
        
        perms = set(perms)
            
        # check if permutation is valid
        
        for j in perms:
            if self.is_valid(j) and j not in temp_list:
                temp_list.append(j)
        
        return temp_list
    
    def is_valid(self, input_str):
        count = 0
        for k in input_str:
            if k == '(':
                count += 1
                
            if k == ')':
                count -= 1
            
            if count < 0:
                return False
        return True

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        temp_list = ['()']
        for i in range(n - 1):

            for j in range(len(temp_list)):

                curr_str = temp_list[j]
                new_str = ''

                for k in range(len(curr_str)):
                    new_str = curr_str[:k] + '()' + curr_str[k:]
                    if new_str not in temp_list:
                        temp_list.append(new_str)
        result = []
        for x in temp_list:
            if len(x) == 2 * n:
                result.append(x)
        return result
