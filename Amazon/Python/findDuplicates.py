# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_list = []
        node_vals = []
        while head:
            
            val = head.val 
            if(val not in node_vals):
                node_list.append(head)
                node_vals.append(val)
            elif(val in node_vals):
                if(node_list and node_list[-1].val == val):
                    node_list.pop()
            head = head.next
        
        # rewire nodes
        if(not node_list):
            return 
        else:
            for i in range(len(node_list)-1):
                curr_node = node_list[i]
                next_node = node_list[i+1]
                curr_node.next = next_node
            node_list[-1].next = None
            return node_list[0]