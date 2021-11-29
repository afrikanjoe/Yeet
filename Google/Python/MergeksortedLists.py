
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def __init__(self):
        self.heap = []
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for node in lists:
            self.add_all_vals(node)
        return self.createLL()
        
        
    def add_all_vals(self,node):
        while node:
            heapq.heappush(self.heap,node.val)
            node = node.next
            
    def createLL(self):
        if(not self.heap):
            return None
        first_val = heapq.heappop(self.heap)
        head = ListNode(first_val)
        temp = head
        while self.heap:
            new_val = heapq.heappop(self.heap)
            new_node = ListNode(new_val)
            temp.next = new_node
            temp = new_node
        return head