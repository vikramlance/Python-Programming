"""
Problem link 
https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


# below solution times out for few test cases but works correctly on other test cases.

import collections

def freqQuery(queries):
    len_queries = len(queries)
    temp = []
    result = []
    for i in range(len_queries):
        if queries[i][0] == 1:
            temp.append(queries[i][1])
        if queries[i][0] == 2 and queries[i][1] in temp:
            temp.remove(queries[i][1])
        if queries[i][0] == 3:
            frequency = queries[i][1]
            dictionary = collections.Counter(temp)
            frequency_match = 0
            for item, count in dictionary.items():
                if count == frequency:
                    frequency_match = 1

            result.append(frequency_match)

    return result


if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))


# below solution times out for one test case but works correctly on all other test cases.

import collections


def freqQuery(queries):
    len_queries = len(queries)
    result = []

    dictionary = {}

    for i in range(len_queries):
        if queries[i][0] == 1:
            j = queries[i][1]
            if j in dictionary:
                dictionary[j] += 1
            else:
                dictionary[j] = 1

        if queries[i][0] == 2 and queries[i][1] in dictionary:
            x = queries[i][1]
            if dictionary[x] > 0:
                dictionary[x] -= 1

        if queries[i][0] == 3:
            frequency = queries[i][1]
            frequency_match = 0

            for k, v in dictionary.items():
                if v == frequency:
                    frequency_match = 1
                    break

            result.append(frequency_match)

    return result


if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))


4
3 4
2 1003
1 16
3 1


10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
"""
import collections


def freqQuery(queries):
    len_queries = len(queries)
    result = []

    dictionary = {}

    frequency_dict = collections.defaultdict(lambda: 0)

    for i in range(len_queries):
        old_count = 0
        new_count = 0
        if queries[i][0] == 1:
            j = queries[i][1]
            if j in dictionary:
                old_count = dictionary[j]
                dictionary[j] += 1
            else:
                dictionary[j] = 1

            new_count = dictionary[j]
            frequency_dict[old_count] -= 1
            frequency_dict[new_count] += 1

        if queries[i][0] == 2 and queries[i][1] in dictionary:
            x = queries[i][1]
            if dictionary[x] > 0:
                old_count = dictionary[x]
                dictionary[x] -= 1
                new_count = dictionary[x]
                frequency_dict[old_count] -= 1
                frequency_dict[new_count] += 1

        if queries[i][0] == 3:
            frequency = queries[i][1]
            frequency_match = 0

            if frequency in frequency_dict:
                if frequency_dict[frequency] > 0:
                    frequency_match = 1

            result.append(frequency_match)

    return result


if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
