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
"""


def sherlockAndAnagrams(s):
    temp = {}
    len_s = len(s)
    pairs = 0
    for i in range(len_s):
        len_substr = i + 1
        for j in range(len_s - i):
            sorted_substr = ''.join(sorted(s[j: j + len_substr]))
            if sorted_substr not in temp:
                temp[sorted_substr] = 0
            else:
                temp[sorted_substr] += 1
                pairs = pairs + temp[sorted_substr]

    return pairs


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
