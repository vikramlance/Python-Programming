"""
Problem link
https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


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
