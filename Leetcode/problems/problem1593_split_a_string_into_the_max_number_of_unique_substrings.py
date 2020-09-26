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

"wwwzfvedwfvhsww"

ababccc

"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        temp_list = []
        i = 0
        last_substring = ''
        while i < len(s):
            # if s[i] is not in temp list then add it
            if s[i] not in temp_list:
                print("hhhhhhhh",s[i])
                temp_list.append(s[i])
                last_substring = s[i]
                i += 1
            # If s[i] is already present in temp list then build a string starting from i-1 and then add one char at a time
            # and keep adding until we find unque string that is not present in temp list , remove old string on top of which 
            # we created the string that we added to the temp list 

            else:
                # temp_list.sort(key = len)
                for j in range(len(s[i:])):
                    print("bbbbbb",s[i:i+j+1])
                    if last_substring + s[i:i+j+1] not in temp_list:
                        print("kkkkk", last_substring + s[i:i+j+1])
                        temp_list.remove(last_substring)
                        temp_list.append(last_substring + s[i:i+j+1])
                        i = i + j + 1
                        break
                temp_list.append(last_substring + s[i:])
                i = i + j + 1
            print("aaaaa",i)
            print(temp_list)
        # print(temp_list)
        return len(temp_list)


test = Solution()

s = "wwwzfvedwfvhsww"     

# a ba b c cc

print(test.maxUniqueSplit(s))
            