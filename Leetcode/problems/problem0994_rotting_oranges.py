"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.


approach 

goto each element 
if its 0 - its empty - do nothing 
if its 1 - its fresh - do notthing
if its 2 - make all cells in 4 directions to 1 -- if any of the cell contain 1, also increase the count

if isolated then take max of all graphs


"""

class solution:
    def num_of_minutes(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        

        for i in range(m):
            for j in range(n):
