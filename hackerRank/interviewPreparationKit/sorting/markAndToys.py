"""
Problem link 
httpswww.hackerrank.comchallengesmark-and-toysproblemh_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

test 
7 50
1 12 5 111 200 1000 10

4

4 50
1 12 5 10

4

4 7
1 2 3 4

3
"""


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    sum_toys = 0
    count_toys = 0
    for i in range(len(prices)):
        sum_toys += prices[i]

        if sum_toys > k:
            count_toys = i
            break
        else:
            count_toys = i + 1

    return count_toys


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')
