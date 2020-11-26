
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        
        from collections import deque
        
        stack_p = deque()
        
        stack_p.append(p)
        
        stack_q = deque()
        stack_q.append(q)
        # result = True
        while stack_q and stack_p:
            
            node_p = stack_p.pop()
            
            node_q = stack_q.pop()
            
            if node_p.val != node_q.val:
                return False
            
            if node_p.left:
                if node_p.left == node_q.left:
                    stack_q.append(node_q.left)
                    stack_p.append(node_p.left)
                else:
                    return False
            
            if node_p.right:
                if node_p.right == node_q.right:
                    stack_q.append(node_q.right)
                    stack_p.append(node_p.right)
                else:
                    return False                                          
        
        return True
        
