import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        
        heap = []
        
        for ls in lists:
            
            while ls:
                heapq.heappush(heap,ls.val)
                ls = ls.next 
        
        head = None
        if(heap):
            head = ListNode(heapq.heappop(heap))
            tmp = head 
            while heap:
                node = ListNode(heapq.heappop(heap))
                tmp.next = node
                tmp = node
        return head
                

