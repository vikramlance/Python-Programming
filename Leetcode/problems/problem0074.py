"""
74. Search a 2D Matrix
Medium

2613

184

Add to List

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix, target):
        # if not matrix :

        # high = matrix[-1][-1]
        # low = matrix[0][0]
    
        row_count = len(matrix)
        if row_count:
            col_count = len(matrix[0])
        else:
            col_count = 0
            
            
        for i in range(row_count):
            for j in range(col_count):
                
                if matrix[i][j] == target:
                    return True
        return False
  
    
