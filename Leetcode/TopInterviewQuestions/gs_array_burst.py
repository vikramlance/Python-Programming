"""
https://leetcode.com/discuss/interview-question/625140/Goldman-Sachs-or-OA-2020-or-Array-Burst-Problem-and-Birthday-Party

Given an input length, String array and burst length(>0) as input, 
the output should be an array which is a shrunk input array such that the sequentially repeating elements 
more than or equal to burst length should be removed. This has to be repeated till the array cannot be shrunk any further. 
Use single characters in the string array for simplicity as shown in sample test cases.

Sample case 1 :
Input :
8
a
b
c
c
c
d
e
e
3
Output:
a
b
d
e
e
"""


def array_burst(input_str, burst_len):

    prev = ''
    curr = ''
    flag = False
    result = ''
    temp = ''


    for i in range(len(input_str)):
        curr = input_str[i]

        if flag and curr == prev:
            if result[len(result)-1] == curr:
                result = result[:len(result)-1]
        elif curr == prev:
            temp = temp + curr
            if len(temp) >= burst_len:
                flag = True

            if i == len(input_str) -1 and not flag:
                result = result + curr
            elif i == len(input_str) -1:
                result = result[:len(result) -1]

        else:
            if not flag and len(temp) > 1:
                result = result + temp[1:] + curr
            else:
                result = result + curr
            temp = curr
            if flag:
                flag = False

        prev = curr

    return result


input_str = 'accccccccccee'

burst_len = 2

print(array_burst(input_str, burst_len))






        