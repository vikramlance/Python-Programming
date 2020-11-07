"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        
        """
        start traversing with bfs 
        
        find the last level
        
        find the first element
        """
                
        from collections import deque
        
        q = deque()              
        q.appendleft(root)        
        curr_level = []        
        curr_level_size = 0        
        
        while q:
            
            curr_level_size = len(q)
            for i in range(curr_level_size):
                
                node = q.pop()
                
                if node.left:
                    curr_level.append(node.left.val)                    
                    q.appendleft(node.left)
                
                if node.right:
                    curr_level.append(node.right.val)                    
                    q.appendleft(node.right)
            
        return curr_level[0]

        
