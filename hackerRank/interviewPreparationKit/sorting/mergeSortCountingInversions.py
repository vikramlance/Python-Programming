"""
Problem link
https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""


def countInversions(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(i + 1, len_arr):
            if arr[i] < arr[j]:
                pass


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result) + '\n')
