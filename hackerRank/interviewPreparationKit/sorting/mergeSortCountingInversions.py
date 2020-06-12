"""
Problem link
https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


# below solution times out for few test cases but works correctly on other test cases.

def is_sorted(input_array):
    for i in range(len(input_array) - 1):
        if input_array[i] > input_array[i + 1]:
            return False
    return True


def countInversions(arr):
    len_arr = len(arr)
    count = 0
    while not is_sorted(arr):
        for i in range(len_arr - 1):
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



# below solution times out for few test cases but works correctly on other test cases.

def countInversions(arr):
    len_arr = len(arr)
    count = 0

    # sorted_array = sorted(arr)
    for i in range(len_arr):
        while i != 0 and arr[i] < arr[i - 1]:
            print("aaaaa", i, arr[i], arr[i - 1])
            temp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = temp
            i -= 1
            count += 1

    return count


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result) + '\n')
"""


def merge(arr, left, right):
    i = 0
    j = 0
    count = 0
    while (i < len(left) or j < len(right)):
        if i == len(left):
            arr[i + j] = right[j]
            j += 1
        elif j == len(right):
            arr[i + j] = left[i]
            i += 1
        elif left[i] <= right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            count += len(left) - i
            j += 1
    return count


def countInversions(arr):
    if len(arr) < 2:
        return 0

    m = int((len(arr) + 1) / 2)
    left = arr[0: m]
    right = arr[m: len(arr)]

    return countInversions(left) + countInversions(right) + merge(arr, left, right)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result) + '\n')
