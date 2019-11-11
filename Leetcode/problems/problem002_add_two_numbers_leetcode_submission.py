"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = ''
        l2_num = ''
        while l1:            
            l1_num += str(l1.val)
            l1 = l1.next
        
        while l2:
            l2_num += str(l2.val)
            l2 = l2.next        
        
        l1_num = int(l1_num[::-1])
        l2_num = int(l2_num[::-1])
        
        number_sum = l1_num + l2_num

        number_sum = str(number_sum)[::-1]
        for i in range(len(number_sum)):
            if i == 0:
                l3 = ListNode(int(number_sum[0]))
                prev_node = l3
            else:
                curr_node = ListNode(int(number_sum[i]))                
                prev_node.next = curr_node
                prev_node = curr_node                

        return l3
