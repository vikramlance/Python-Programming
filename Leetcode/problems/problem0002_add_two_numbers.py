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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_last_digit = l1.val
        l1_middle_digit = l1.next.val
        l1_first_digit = l1.next.next.val

        l2_last_digit = l2.val
        l2_middle_digit = l2.next.val
        l2_first_digit = l2.next.next.val

        number_sum = (l1_first_digit*100 + l1_middle_digit*10 + l1_last_digit) + (l2_first_digit*100 + l2_middle_digit*10 + l2_last_digit)

        number_sum = str(number_sum)
        l3 = ListNode(int(number_sum[2]))
        l3.next = ListNode(int(number_sum[1]))
        l3.next.next = ListNode(int(number_sum[0]))

        return l3.val, l3.next.val, l3.next.next.val


out_solution = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

output = out_solution.addTwoNumbers(l1, l2)

print(output)
