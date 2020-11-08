"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal. 

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:              
        from collections import deque        
        if not root:
            return 0
        q = deque()
        q.appendleft(root)
        
        max_sum_level = 1
        max_sum = root.val
        
        curr_level = 0
        curr_level_sum = 0
        
        while q:            
            for i in range(len(q)):
                curr_node = q.pop()                
                curr_level_sum += curr_node.val
                if curr_node.left:
                    q.appendleft(curr_node.left)
                if curr_node.right:
                    q.appendleft(curr_node.right)
            
            curr_level += 1
            if max_sum < curr_level_sum:
                max_sum = curr_level_sum
                max_sum_level = curr_level                               
            curr_level_sum = 0 
        return max_sum_level


# [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]

t11= TreeNode(val=5, left=None, right=None)
t10= TreeNode(val=4, left=None, right=None)
t9 = TreeNode(val=1, left=None, right=None )
t8 = TreeNode(val=9, left=None, right=None )
t7 = TreeNode(val=3, left=None, right=t11 )
t6 = TreeNode(val=1, left=None, right=None )

t5 = TreeNode(val=7, left=t9, right=t10 )
t4 = TreeNode(val=2, left=t8, right=None )
t3 = TreeNode(val=8, left=t6, right=t7 )
t2= TreeNode(val=7, left=t4, right=t5 )

t1 = TreeNode(val=6, left=t2, right=t3 )

test = Solution()

print(test.maxLevelSum(t1))      