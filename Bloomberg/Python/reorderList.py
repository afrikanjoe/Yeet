"""
You are given the head of a singly linked-list. The list can be represented as:

reorder if from this to  
L0 -> L1 -> ... -> Ln - 1 -> Ln

this
L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        vals = []
        while head:
            vals.append(head)
            head = head.next
        if(not vals):
            pass
        else:
            count = 1
            head = vals[0]
            tmp = head
            vals.pop(0)
            while vals:
                if(count%2==1):
                    new_node = vals.pop()
                else:
                    new_node = vals.pop(0)
                tmp.next = new_node
                tmp = new_node
                count+=1
            tmp.next = None