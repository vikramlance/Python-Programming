"""Module to find out longest substring without repeatition

Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        max_str = ''
        for i in range(len(s)):
          lookup_str = ''
          curr_str = ''
          for j in s[i:]:
            curr_str += j
            if j in lookup_str:
              if len(lookup_str) > max_len:
                max_len = len(lookup_str) 
                max_str = lookup_str
              break
            else:
              lookup_str += j
              if len(lookup_str) > max_len:
                max_len = len(lookup_str) 
                max_str = lookup_str
        return max_len

input_list = ['aab', 'abcabdcca', 'bbbbbbb', '  ']   
sol1 = Solution()
for i in input_list:
  print(sol1.lengthOfLongestSubstring(i))
