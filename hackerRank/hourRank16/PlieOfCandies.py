'''
problem statement
https://www.hackerrank.com/contests/hourrank-16/challenges/pile-of-candies

input
100
13 57 37 57 54 17 28 56 30 29 60 54 59 53 13 52 56 45 35 35 46 18 49 61 47 54 41 57 36 51 51 37 46 28 35 40 35 51 34 54 20 34 48 17 26 49 58 22 34 33 46 21 40 33 22 27 27 53 22 51 42 13 29 29 30 52 57 53 41 30 47 51 54 34 57 20 23 55 31 48 28 15 57 58 38 19 24 56 61 34 47 43 36 14 60 54 56 58 45 37

output
13 100

input
1
10

output
20 1

input 
9
10 4 10 20 20 30 30 7 8

output
7 1
'''

#!/bin/python
import sys

n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' '))

c.sort()

mini = c[0]
if n>1:
    happiness_list= [(2*mini),(c[1])]
    happiness = min(happiness_list)
    if (2*mini) > (c[1]) and c.count(mini) > 1:
        count= n
    else:
        count = c.count(mini)
else:
    happiness = 2*mini
    count=n

print (str(happiness)+" "+str(count))



