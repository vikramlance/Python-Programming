"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth_bfs(self, root):
        if not root:
            return 0
        from collections import deque
        
        q = deque()
        q.appendleft(root)
        
        depth = 0
        
        while q:
            
            for i in range(len(q)):
                
                node = q.pop()
                
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                    
            depth += 1
        return depth


    def maxDepth_dfs(self, root):
        if not root:
            return 0

        max_left = self.maxDepth_dfs(root.left)
        max_right = self.maxDepth_dfs(root.right)

        max_depth = max(max_left, max_right)

        return max_depth + 1 


        