"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if(head == None):
            return head
        vals = []
        new_head = ListNode()
        while(head):
            if(head.val in vals):
                vals = vals
            else:
                vals.append(head.val)
            head = head.next
        
        new_head.val = vals[0]
        temp = new_head
        for i in vals[1:]:
            print(i)
            new_node = ListNode(i)
            temp.next = new_node
            temp = new_node
        return new_head