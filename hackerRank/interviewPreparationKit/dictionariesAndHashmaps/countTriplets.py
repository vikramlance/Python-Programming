"""
Problem link
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

test input
4 2
1 2 2 4

output
2

i 0 1

temp {
    0: [1, 2, 4]
    1: [2, 4]
    2: [2, 4]
    3: [4]
}

0: [1, 2]
1: [2]
3: [3]
4: [2]
5: [4]
"""


def countTriplets(arr, r):
    triplets = 0
    len_arr = len(arr)
    temp = {}

    for i in range(len_arr):
        temp[i] = [arr[i]]
        for j in temp:
            if len(temp[j]) == 1 and temp[j][0] * r == arr[i]:
                temp[i].append(arr[i])
            if len(temp[j]) == 2 and temp[j][1] * r == arr[i]:
                temp[i].append(arr[i])

            if len(temp[j]) == 3:
                triplets += 1

    return triplets


if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

   print(str(ans))
