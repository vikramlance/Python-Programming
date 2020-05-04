""" problem link
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he
took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, D step. Gary's hikes start and end at sea
level and each step up or down represents a 1 unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down
to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to
sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
For example, if Gary's path is s = [DDUUUUDD], he first enters a valley 2 units deep. Then he climbs out an up onto a mountain
2 units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    valley_num = 0
    temp = []
    for i in  range(n):
        if s[i]=='U':
            sea_level = sea_level + 1
        if s[i]=='D':
            sea_level = sea_level - 1
        if sea_level == 0:
            if any(n < 0 for n in temp):
                valley_num = valley_num + 1
            temp = []
        else:
            temp.append(sea_level)

    return valley_num
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
