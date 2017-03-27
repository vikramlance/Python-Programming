'''
Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.

Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
'''
#!/bin/python

import re
import sys


n = int(raw_input().strip())

a=bin(n)
print a

print (max(len(s) for s in re.findall(r'1+', a)))


#"{0:#b}".format(n)
