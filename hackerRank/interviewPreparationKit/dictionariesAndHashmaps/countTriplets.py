"""
Problem link
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

test input
4 2
1 2 2 4

output
2

test input
4 2
1 2 2 4
output
2

test input
6 3
1 3 9 9 27 81
output
6

test input
100 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
output
161700

# This solution fails the above test (r=1) and times out for few other test cases

def countTriplets(arr, r):
    triplets = 0
    len_arr = len(arr)
    temp = {}

    for i in range(len_arr):
        temp[i] = [arr[i], 0]

        for j in temp:
            if len(temp[j]) == 2:
                if temp[j][0] == arr[i]:
                    if temp.get(j - 1):
                        if temp[j - 1][0] != arr[i]:
                            temp[j][1] += 1
                    else:
                        temp[j][1] += 1
                if temp[j][0] * r == arr[i]:
                    temp[j].extend([arr[i], 0])
            if len(temp[j]) == 4:
                if temp[j][2] == arr[i]:
                    temp[j][3] += 1
                if temp[j][2] * r == arr[i]:
                    temp[j].extend([arr[i], 0])

            if len(temp[j]) == 6:
                if temp[j][4] == arr[i]:
                    temp[j][5] += 1

    for k in temp:
        if len(temp[k]) == 6:
            triplets += temp[k][1] * temp[k][3] * temp[k][5]

    return triplets


if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans))


"""
from collections import defaultdict


def countTriplets(arr, r):
    triplet = 0
    arr_len = len(arr)

    first_item = defaultdict(lambda: 0)
    third_item = defaultdict(lambda: 0)

    # traverse through the elements
    for i in range(arr_len):
        third_item[arr[i]] += 1  # keep the count in the hash

    # traverse through all elements and
    # find out the number of elements as k1*k2

    for i in range(len_arr):
        # keep the count of left and right elements
        # left is arr[i]/r and right arr[i]*r
        c1, c2 = 0, 0

        # if the current element is divisible
        # by r, count elements in first item hash.
        if arr[i] % r == 0:
            c1 = first_item[arr[i] // r]

        # decrease the count in right hash
        third_item[arr[i]] -= 1

        # number of right elements
        c2 = third_item[arr[i] * r]

        # calculate the answer
        triplet += c1 * c2

        first_item[arr[i]] += 1  # left count of arr[i]

    return triplet


if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans))
