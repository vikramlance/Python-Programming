"""
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root):
        
        def dfs(curr_node, result):    
            if not curr_node:
                return result

            left = curr_node.left
            right = curr_node.right

            if curr_node.val % 2 == 0:                           
                if left:
                    if left.left:
                        result += (left.left.val or 0) 
                    if left.right:
                        result += (left.right.val or 0)
                    
                if right:
                    if right.left:
                        result += (right.left.val or 0) 
                    if right.right:
                        result += (right.right.val or 0)  
            if left:
                result = dfs(left, result)
            if right:
                result = dfs(right, result)

            return result
                    
        output = dfs(root, 0)

        return output


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

print(test.sumEvenGrandparent(t1))