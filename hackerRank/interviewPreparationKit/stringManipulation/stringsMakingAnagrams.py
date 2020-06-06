"""
Problem link
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""


def makeAnagram(a, b):
    temp_a = {}
    temp_b = {}
    for i in a:
        if i in temp_a:
            temp_a[i] += 1
        else:
            temp_a[i] = 1

    for i in b:
        if i in temp_b:
            temp_b[i] += 1
        else:
            temp_b[i] = 1
    count = 0
    for j in temp_a:
        if j in temp_b:
            count += abs(temp_a[j] - temp_b[j])
        else:
            count += temp_a[j]
    for k in temp_b:
        if k not in temp_a:
            count += temp_b[k]

    return count


if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(str(res) + '\n')
