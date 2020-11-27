
"""
5479. Thousand Separator
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 

Constraints:

0 <= n < 2^31

convert int to str 

read str in reverse

after every 3 chars add .

run the loop until the str is complete

"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n_str = str(n)
        new_str = ''

        reverse_str = n_str[::-1]


        for i in range(len(n_str)):
            if i % 3 == 0:

                new_str = new_str + "." +  reverse_str[i:i+3] 

        reverse_new_str = new_str[::-1]
        return reverse_new_str[:len(reverse_new_str) -1]



test = Solution()

n = 987
print(test.thousandSeparator(n))

n = 1234
print(test.thousandSeparator(n))

n = 123456789
print(test.thousandSeparator(n))

n = 0
print(test.thousandSeparator(n))