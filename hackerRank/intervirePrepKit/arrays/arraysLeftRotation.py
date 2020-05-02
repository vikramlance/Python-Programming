"""
Problem link
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    partial_array_end = a[d:]
    partial_array_start = a[:d]
    partial_array_end.extend(partial_array_start)

    return partial_array_end


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
