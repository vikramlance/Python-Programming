"""
Problem link
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

test

9 5
2 3 4 2 3 6 8 4 5

2

# below solution times out for few test cases but works correctly on other test cases.

def median(arr):
    med = 0
    l = len(arr)
    arr.sort()
    if (l % 2) == 0:
        med = (arr[int(l / 2)] + arr[int((l + 1) / 2)]) / 2
    else:
        med = arr[int((l - 1) / 2)]

    return med


def activityNotifications(expenditure, d):
    count = 0
    len_e = len(expenditure)
    for i in range(d, len_e):
        # print(i, expenditure[i - d:i], median(expenditure[i - d:i]))
        if median(expenditure[i - d:i]) * 2 <= expenditure[i]:
            count += 1
    return count


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')


--------------

from collections import deque

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
   # k << d, n --> counting sort approach
    k = max(expenditure)
    historic_counts = [0] * (k+1)
    trailing_history = deque([])
    num_notifications = 0

    for day in range(len(expenditure)):
        if day >= d:
            if expenditure[day] >= 2 * median(historic_counts, d):
                num_notifications += 1

            historic_counts[trailing_history.popleft()] -= 1

        historic_counts[expenditure[day]] += 1
        trailing_history.append(expenditure[day])

    return num_notifications

def median(idx_counts, d):
    # if d is odd, the median is found at idx
        # d_half_floored +1 = d//2 + 1
    # if d is even, the median is the mean of elements
        # at idcs d_half_floored and d_half_floored + 1
    d_half_floored = d // 2
    median_low = 0
    median_high = 0
    traversed_elements = idx_counts[0]

    idx = 1
    while traversed_elements <= d_half_floored:
        median_high = idx
        if traversed_elements < d_half_floored:
            median_low = idx  # still too low

        traversed_elements += idx_counts[idx]
        idx += 1
            
    if d % 2 != 0:
        return median_high  # d is odd
    else:
        return (median_low + median_high) / 2  # d is even

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')

"""
import bisect 
import statistics

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
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list

def median(lst):
    n = len(lst)
    s = counting_sort(lst)
    return (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2] if n else None



# def median(arr):
#     med = 0
#     l = len(arr)
#     arr.sort()
#     if (l % 2) == 0:
#         med = (arr[int(l / 2)] + arr[int((l + 1) / 2)]) / 2
#     else:
#         med = arr[int((l - 1) / 2)]

#     return med


# def activityNotifications(expenditure, d):
#     count = 0
#     len_e = len(expenditure)
#     sorted_e = sorted(expenditure[0:d])
#     for i in range(d, len_e):
        
#         if i == d:
#             sorted_slice = sorted_e
#             if median(sorted_slice) * 2 <= expenditure[i]:
#                 count += 1
#             # print(i, sorted_slice, median(sorted_slice))
#         else:
#             temp_list = sorted_slice[1:]
#             bisect.insort(temp_list, expenditure[i])  
#             sorted_slice = temp_list
#             if median(temp_list) * 2 <= expenditure[i]:
#                 count += 1
#             # print(i, temp_list, median(temp_list))
#     return count

def activityNotifications(expenditure, d):
    count = 0
    len_e = len(expenditure)
    for i in range(d, len_e):
        # print(i, expenditure[i - d:i], median(expenditure[i - d:i]))  -- median(expenditure[i - d:i])
        if statistics.median(expenditure[i - d:i]) * 2 <= expenditure[i]:
            count += 1
    return count

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
