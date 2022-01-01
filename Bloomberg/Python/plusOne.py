# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        nums = ""
        while head:
            nums += str(head.val)
            head = head.next
        
        nums = list(str(int(nums)+1))
        
        head = ListNode(int(nums[0]))
        temp = head
        for i in range(1,len(nums)):
            
            new_node = ListNode(int(nums[i]))
            temp.next = new_node
            temp = new_node
        return head
            

    