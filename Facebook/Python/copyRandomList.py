"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head 
        
        node_dict = {head:Node(head.val)}
        node_iter = head
        while node_iter.next!=None:
            node = node_iter.next
            node_dict[node] = Node(node.val)
            node_iter = node
       
        # do the wiring
        node_iter = head
        while node_iter!=None:
            if(node_iter.next):
                node_dict[node_iter].next = node_dict[node_iter.next]
            node_dict[node_iter].random = node_dict.get(node_iter.random,None)
            node_iter = node_iter.next
            
        return node_dict[head]
        
        
