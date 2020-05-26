"""
Problem link 

https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""


def countSwaps(a):
    counter = 0
    n = len(a)
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                counter += 1

    return counter, a[0], a[n - 1]


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    counter, first_element, last_element = countSwaps(a)

    print("Array is sorted in " + str(counter) + " swaps.")
    print("First Element: " + str(first_element))
    print("Last Element: " + str(last_element))
