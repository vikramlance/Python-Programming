"""
Problem link
https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


"""
-----------------------------------------------------------------
# below solution times out for few test cases but works correctly on other test cases.

def arrayManipulation(n, queries):
    len_queries = len(queries)
    arr = [0] * n
    for i in range(len_queries):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]

        for j in range(a - 1, b):
            arr[j] = arr[j] + k

    return max(arr)


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

-----------------------------------------------------------------
# below solution times out for few test cases but works correctly on other test cases.

import operator


def arrayManipulation(n, queries):
    len_queries = len(queries)
    arr = [0] * n
    temp = {}
    max_sum = 0

    for i in range(len_queries):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]

        for j in range(a - 1, b):
            if j in temp:
                temp[j] = temp[j] + k
            else:
                temp[j] = k

    max_sum = max(temp.items(), key=operator.itemgetter(1))[1]
    return max_sum


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

"""


def arrayManipulation(n, queries):
    len_queries = len(queries)
    arr = [0] * n
    max_sum = 0
    index_sum = 0

    for i in range(len_queries):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]

        # add +k at arr[a - 1] and -k at arr[b]
        arr[a - 1] = arr[a - 1] + k
        if b != n:
            arr[b] = arr[b] - k

    for j in range(len(arr)):
        index_sum = index_sum + arr[j]
        if index_sum > max_sum:
            max_sum = index_sum

    return max_sum


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
