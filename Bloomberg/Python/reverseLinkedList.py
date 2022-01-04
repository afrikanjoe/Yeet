"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
        prev = None
        curr_node = head
        while curr_node:
            tmp = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = tmp 
        
        return prev

     def reverseList(self, head):
        
        def helper(prev,head):
            if(head.next == None):
                head.next = prev
                return head
            else:
                tmp = head.next 
                head.next = prev
                return helper(head,tmp)
        if(not head):
            return 
        return helper(None,head)
        