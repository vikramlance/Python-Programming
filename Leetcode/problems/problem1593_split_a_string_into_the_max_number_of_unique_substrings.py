"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.

ababccc

"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        temp_list = []
        i = 0
        while i < len(s):
            if s[i] not in temp_list:
                temp_list.append(s[i])
                i += 1
            # find item with minimum lengh in temp_list and append s[i] to it and see if its unique repeat if not
            else:
                # temp_list.sort(key = len)
                for j in range(len(s[i+1:])):
                    if s[i:i+j+2] not in temp_list:
                        temp_list.append(s[i:j])
                        i = i + j +2
                        break
        print(temp_list)
        return len(temp_list)



test = Solution()

s = "ababccc"     

print(test.maxUniqueSplit(s))
            