"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        for i in range(0,len(nodes),2):
            
            if(i+1<len(nodes)):
                
                temp = nodes[i]
                nodes[i] = nodes[i+1]
                nodes[i+1] = temp
                
        for i in range(len(nodes)-1):
            
            node_a = nodes[i]
            node_b = nodes[i+1]
            node_a.next = node_b
            
        if(nodes):
            nodes[-1].next = None
            return nodes[0]
            