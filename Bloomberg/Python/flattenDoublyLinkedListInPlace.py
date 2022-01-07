"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        
        #head_tmp = head
        def flatten_helper(head_tmp):
            
            # skip if you don't have a child
            while head_tmp.next and not head_tmp.child:
                head_tmp = head_tmp.next 
                
            if(not head_tmp.child):
                return head_tmp
            else:
                last_node = flatten_helper(head_tmp.child)
                tmp = head_tmp.next
                
                # set my next to be my child
                head_tmp.next = head_tmp.child
                
                # set my child's previous to me
                head_tmp.child.prev = head_tmp
                
                head_tmp.child = None
                
                #print(head_tmp.val,head_tmp.next.val,head_tmp.next.prev.val)
                
                if(tmp):
                    last_node.next = tmp
                    tmp.prev = last_node
                
                    return flatten_helper(tmp)
                else:
                    return last_node
        
        if(head):
            _ = flatten_helper(head)
        
#         while head:
#             if(head.prev):
#                 print(head.val,head.prev.val)
#             head = head.next
        
        return head
            