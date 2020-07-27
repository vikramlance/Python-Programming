"""

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class zigzag_traversal_solution:
    def traverse_zigzag(self, arr):
        result = []
        temp_queue = deque()
        temp_queue.append(arr[0])
        i = 0
        level_number = 1
        while temp_queue:
            
            current_level_nodes = []
            temp_queue_len = len(temp_queue)
            for j in range(temp_queue_len ):
                curr_node = temp_queue.popleft()
                current_level_nodes.append(curr_node )
                # add children of curr node to the temp queue
                if 2*i + 1 < len(arr) and arr[2*i + 1]:
                    temp_queue.append(arr[2*i + 1])
                if 2*i + 2 < len(arr) and arr[2*i + 2]:
                    temp_queue.append(arr[2*i + 2])

                i += 1
            if level_number % 2 == 0:               
                result.append(current_level_nodes[::-1] )
            else:                    
                result.append(current_level_nodes)
            level_number += 1
        return result

test = zigzag_traversal_solution()
arr = [3,9,20,None,None,15,7]
print(test.traverse_zigzag(arr))
