#!/bin/python3
"""
problem link

https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud.
It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
For example, indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes and .
She could follow the following two paths: or . The first path takes jumps while the second takes .
c = [0,1,0,0,0,1,0]
0...6150->2->4->60->2->3->4->634

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers

Input Format

The first line contains an integer n, the total number of clouds. The second line contains n space-separated binary integers describing clouds where .
c[i]0<=i<n

Output Format

Print the minimum number of jumps needed to win the game.

"""
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    curr = 0
    jumps = 0
    num_clouds = len(c)
    for i in range(num_clouds):
        if curr in (num_clouds - 2, num_clouds - 3):
            jumps = jumps + 1
            break

        if c[curr + 2] == 1:
            curr = curr + 1
        else:
            curr = curr + 2

        jumps = jumps + 1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
