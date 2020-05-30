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


def median(lst):
    n = len(lst)
    s = sorted(lst)
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
