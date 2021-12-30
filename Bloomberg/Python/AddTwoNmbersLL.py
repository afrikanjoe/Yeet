# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        num = ""
        while l1:
            num = num + str(l1.val)
            l1 = l1.next
        num2 = ""
        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        
        ans = list(str(int(num) + int(num2)))
        
        head = ListNode(int(ans[0]))
        temp = head
        
        for i in ans[1:]:
            
            new_node = ListNode(int(i))
            temp.next = new_node
            temp = new_node
        return head
            