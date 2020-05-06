"""
Problem link
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

"""
# below solution times out for few test cases but works correctly on other test cases.
def minimumSwaps(arr):
    len_arr = len(arr)
    swap_num = 0

    for i in range(len_arr):
        if arr[i] != i + 1:
            arr[arr.index(i + 1)] = arr[i]
            arr[i] = i + 1
            swap_num = swap_num + 1

    return swap_num


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

"""


def minimumSwaps(arr):
    len_arr = len(arr)
    swap_num = 0
    temp = 0
    for i in range(len_arr):
        while arr[i] != i + 1:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swap_num = swap_num + 1

    return swap_num


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
