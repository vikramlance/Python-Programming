'''
https://www.hackerrank.com/challenges/designer-pdf-viewer
'''


#!/bin/python3

import sys




size = [int(i) for i in input().split()]
word = [size[ord(c)-ord('a')] for c in input()]
print (max(word)*len(word))
