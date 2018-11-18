"""Module to find out longest substring without repeatition

Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

class longestSubstring():

    def longest_substring_without_rep(self, Input):
        longest = ''
        longest_temp = ''

        for i in Input:
            if i not in longest_temp:
                longest_temp += i
            else:
                if len(longest) < len(longest_temp):
                    longest = longest_temp
                longest_temp = i

        return len(longest)

test = longestSubstring()

print(test.longest_substring_without_rep("abcabcdbb"))

print(test.longest_substring_without_rep("bbbbb"))

