"""
Problem link
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    length_q = len(q)
    bribe_count = 0
    temp = []

    for i in range(length_q):
        if q[i] > i + 3:
            return 'Too chaotic'

        if q[i] == i + 2:
            bribe_count = bribe_count + 1

        if q[i] == i + 3:
            bribe_count = bribe_count + 2

        if i + 1 not in (q[i - 1], q[i - 2]):
            temp.append(i + 1)

        if q[i] in temp:
            if temp.index(q[i]) > 2:
                return 'Too chaotic'
            if temp.index(q[i]) == 2:
                bribe_count = bribe_count + 2
            if temp.index(q[i]) == 1:
                bribe_count = bribe_count + 1

            temp.remove(q[i])

    return bribe_count


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        min_bribes = minimumBribes(q)

        print(min_bribes)
