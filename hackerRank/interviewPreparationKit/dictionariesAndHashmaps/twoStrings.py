"""
Problem link
https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

test case 1

2
hello
world
hi
world


-----------------------------------------------------------------
# Using set intersection.


def twoStrings(s1, s2):

    if set(s1).intersection(s2):
        return 'YES'
    return 'NO'


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)

"""


def twoStrings(s1, s2):
    s1_dict = {}
    for i in s1:
        if i not in s1_dict:
            s1_dict[i] = 1

    for j in s2:
        if j in s1_dict:
            return 'YES'

    return 'NO'


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
