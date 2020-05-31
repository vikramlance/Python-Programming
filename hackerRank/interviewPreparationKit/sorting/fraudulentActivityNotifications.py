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
"""
import bisect 

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
