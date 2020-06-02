"""
Problem link
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

test

9 5
2 3 4 2 3 6 8 4 5

2


"""
import bisect
from collections import deque
def counting_sort(the_list):

    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input
    # etc.
    counts = [0] * (201)
    for item in the_list:
        counts[item] += 1

    # Overwrite counts to hold the next index an item with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has.
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(the_list)

    # Run through the input list
    for item in the_list:

        # Place the item in the sorted list
        sorted_list[counts[item]] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list


def median(arr, d, last_element):
    med = 0
    # l = len(arr)  1 2 3 4 5 2.5
    arr = counting_sort(arr)
    if (d % 2) == 0:
        if arr[int(d / 2)]
        med = (arr[int(d / 2)] + arr[int((d + 1) / 2)]) / 2
    else:
        med = arr[int((d - 1) / 2)]

    return med


def activityNotifications(expenditure, d):
    count = 0
    len_e = len(expenditure)
    sorted_e = sorted(expenditure[0:d])
    sorted_deque = deque(sorted_e)
    for i in range(d, len_e):
        if i == d:
            # sorted_slice = sorted_deque
            if median(sorted_deque) * 2 <= expenditure[i]:
                count += 1
            # print(i, sorted_slice, median(sorted_slice))
        else:
            temp_list = sorted_deque
            bisect.insort(temp_list, expenditure[i])
            sorted_deque = temp_list
            if median(temp_list) * 2 <= expenditure[i]:
                count += 1
            # print(i, temp_list, median(temp_list))
    return count


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
