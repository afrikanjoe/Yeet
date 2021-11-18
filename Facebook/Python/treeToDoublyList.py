

import heapq

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        if(not root):
            return 
        queue = [root]
        node_dict = {}
        value_heap = []
        while queue: 
            node = queue.pop(0)
            heapq.heappush(value_heap,node.val)
            node_dict[node.val] = node
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        
        first = node_dict[value_heap[0]]
        for i in range(len(value_heap)-1):
            min_val = heapq.heappop(value_heap)
            next_smallest = value_heap[0]
            node_a = node_dict[min_val]
            node_b = node_dict[next_smallest]
            
            node_a.right = node_b
            node_b.left = node_a
            
        last = node_dict[value_heap[0]]
        first.left = last
        last.right = first
        
        return first
