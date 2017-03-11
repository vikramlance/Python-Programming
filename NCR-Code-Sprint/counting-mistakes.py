'''
refer pdf doc for problem statement
'''

#!/bin/python
import sys

n = int(raw_input().strip())
starList= map(int, raw_input().split())
m=len(starList)
count=0
oldStar=starList[0]
for i in range(m):
    if i==0:
        if starList[i] !=1 :
            count+=1
    else:
        newStar=starList[i]
        if newStar !=oldStar + 1:
            count+=1
        oldStar=newStar
print count
