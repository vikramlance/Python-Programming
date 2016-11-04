'''
https://www.hackerrank.com/challenges/pangrams
'''

import string
s= raw_input()

s=s.lower()

for i in list(string.ascii_lowercase):
    
    if i not in s:
        print "not pangram"
        quit()

print "pangram"
