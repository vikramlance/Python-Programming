"""
Problem link
https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""


def is_sorted(input_array):
    for i in range(len(input_array) - 1):
        if input_array[i] > input_array[i + 1]:
            return False
    return True


def countInversions(arr):
    len_arr = len(arr)
    count = 0
    while not is_sorted(arr):
        for i in range(len_arr):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                count += 1

    return count


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result) + '\n')
