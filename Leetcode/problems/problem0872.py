"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        leaf_value_sequence_1 = self.get_sequence(root1)
        leaf_value_sequence_2 = self.get_sequence(root2)
        result = False
        if leaf_value_sequence_1 == leaf_value_sequence_2:
            result = True
        return result
    
    
    def get_sequence(self, root):
        # visited = set()
        from collections import deque
        
        stack = deque()
        result = []
        
        stack.append(root)
        # visited.add(root)
        
        while stack:
            
            node = stack.pop()
            
            # if node.left and node.left not in visited:
            if node.left:
                stack.append(node.left)
            
            # if node.right and node.right not in visited:
            if node.right:
                stack.append(node.right)
            
            if not node.left and not node.right:
                result.append(node.val)
        return result 
                        