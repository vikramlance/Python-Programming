""" problem link
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""
#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    string_length = len(s)

    count_a = s.count('a')

    full_strings_num, partial_string_length = divmod(n, string_length)

    count_a_total = full_strings_num * count_a + \
        s[0:partial_string_length].count('a')

    return count_a_total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
