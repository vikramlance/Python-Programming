"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

def largest_palindromic_substr(input_str):
    """ First check each element in the string 
        for each element check if it is a starting element of a palindrome
        - 
    """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        input_str = s
        input_str = list(input_str)
        size = len(input_str)
        longest_palindrome = ''
        for i, _value in enumerate(input_str):
            print(i, _value)
            if _value in input_str[i+1:]:
                index_list = self.indicesOfDuplicateElements(_value, input_str[i+1:]) 
                print("fdksjd")
                print(index_list)
                for j in index_list:
                    if len(input_str[i:j]) > len(longest_palindrome):
                        print("asd")
                        print(input_str[i:j])
                        if self.isPalindrome(input_str[i:j]):
                            longest_palindrome = input_str[i:j]

        return "".join(longest_palindrome)       


    def isPalindrome(self, sub_string):

        sub_string = list(sub_string)
        size = len(sub_string)


        result = True if sub_string == sub_string[::-1] else False

        return result

    # print(isPalindrome("aba"))

    def indicesOfDuplicateElements(self, element, in_string):
        in_string = list(in_string)
        size = len(in_string)
        index_list = []
        for element in in_string:
            index_list.append(in_string.index(element))

        return index_list        

 
print(largest_palindromic_substr("asdsas"))
