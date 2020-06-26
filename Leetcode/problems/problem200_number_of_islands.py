"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class solution:

    def num_of_islands(self, grid):
        num_rows = len(grid)
        num_columns = len(grid[0]) if num_rows else 0
        count = 0

        for x in range(num_rows):
            for y in range(num_columns):
                # check left and top elements of current element
                # if its not 1 and current element is 1 then increase count

                # first element of grid
                if x == 0 and y == 0 and grid[x][y] == '1':
                    count += 1
                # first row of grid except first element of grid
                if x == 0 and y != 0 and grid[x][y] == '1' and grid[x][y - 1] == '0':
                    count += 1

                # first column of grid except first element of grid
                if x != 0 and y == 0 and grid[x][y] == '1' and grid[x - 1][y] == '0':
                    count += 1
                # all the reamining elements
                if x != 0 and y != 0 and grid[x][y] == '1' and grid[x][y - 1] == '0' and grid[x - 1][y] == '0':
                    count += 1

        return count


grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
        ]

test = solution()
print(test.num_of_islands(grid))


grid = [["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]]

test = solution()
print(test.num_of_islands(grid))
