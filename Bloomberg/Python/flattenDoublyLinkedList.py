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
    
    def __init__(self):
        self.nodes = []
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def flatten_helper(node):
            if(not node):
                return 
            self.nodes.append(node)
            flatten_helper(node.child)
            flatten_helper(node.next)
        
        flatten_helper(head)
        if(not self.nodes):
            return 
        self.nodes[0].prev = None
        self.nodes[-1].next = None
        self.nodes[-1].child = None 
        for i in range(0,len(self.nodes)-1):
            
            node_a =self.nodes[i]
            node_b = self.nodes[i+1]
            node_a.child = None
            node_a.next = node_b
            node_b.prev = node_a
            node_b.child = None
            
        return self.nodes[0]