"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
 
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result =[]
        char_list = list(S)
        
        # store last occurence index as value and letter as key in the temp dictionary 
        temp_dict = {}
        
        for i in range(len(char_list)):
            temp_dict[char_list[i]] = i
            
        # { 'a':9, 'b':18}
        
        start = 0 
        
        max_last_index = 0
        for j in range(len(char_list)):
            
            max_last_index = max(max_last_index, temp_dict[char_list[j]])
            
            if max_last_index == j:
                
                curr_substring_len = max_last_index - start + 1 
                result.append(curr_substring_len)
                start = j + 1
            
        return result
        
            
        