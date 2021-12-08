"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        
        node_list = []
        
        while head:
            node_list.append(head)
            head = head.next 
        
        # remove node
        
        index = len(node_list) - n
        if(index == 0):
            if(len(node_list)>1):
                return node_list[1]
        else:
            prev = node_list[index-1]
            deln = node_list[index]
            
            prev.next = deln.next
            return node_list[0]