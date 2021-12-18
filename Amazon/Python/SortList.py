# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        heap = []
        
        while head: 
            heapq.heappush(heap,head.val)
            head = head.next
        if not heap:
            return
        head = ListNode(heapq.heappop(heap))
        temp = head 
        
        while len(heap)>0: 
            curr_node = ListNode(heapq.heappop(heap))
            temp.next = curr_node
            temp = curr_node
            
        temp.next = None
        return head
            
        