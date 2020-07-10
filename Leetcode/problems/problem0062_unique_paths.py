"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 
Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.


------- 
# wrong answer with recursion
class solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < 1:
            return 0
        i = 0
        j = 0
        count = 0
        # for i in range(m):
        #     for j in range(n):
        count = self.paths(i, j, m, n)
        return count

    def paths(self, i, j, m, n):
        if i == 0 and j == 0:
            count = 0

        if i < m and j < n:
            if i == m - 1 and j == n - 1:
                return 1
            print(i, j)
            print("count1", count)
            count = count + self.paths(i + 1, j, m, n)
            print("count2", count)
            count = count + self.paths(i, j + 1, m, n)
            print("count3", count)

        return count

"""


class solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0

        grid = [[0] * n] * m
        for i in range(m):
            for j in range(n):

                if (i == 0 and j < n) or (j == 0 and i < m):
                    grid[i][j] = 1

                elif i < m and j < n:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

                if i == m - 1 and j == n - 1:
                    return grid[i][j]


test = solution()

print(test.uniquePaths(3, 2))
