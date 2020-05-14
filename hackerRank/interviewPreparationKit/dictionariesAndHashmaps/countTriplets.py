"""
Problem link
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""


def countTriplets(arr, r):
    triplets = 0
    len_arr = len(arr)
    for i in range(len_arr - 2):
        if i * r in arr[i + 1:len_arr - 1] and i * r * r in arr[i + 2:len_arr] and indexof(i * r) < indexof(i * r * r):
            triplets += 1
    return triplets


if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

   print(str(ans))
