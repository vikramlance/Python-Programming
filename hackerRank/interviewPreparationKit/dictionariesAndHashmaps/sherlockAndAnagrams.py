"""
Problem link
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

test 
2
ifailuhkqq
kkkk

output 
3
10

i:1
f:2
a:3
i:4
l:5
u:6
h:7
k:8
q:9
q:10

ii 
iaf : fai
qq

"""

from itertools import combinations


def sherlockAndAnagrams(s):
    temp = {}

    for i in range(len(s)):
        for j in combinations(s, i):
            if j in temp:
                temp[j] += 1
            else:
                temp[j] = 0
    pairs = 0
    for j in temp:
        if temp[j] > 1:
            pairs = pairs + temp[j]
    return pairs


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
