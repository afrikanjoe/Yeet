"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        
        depth_dict = {}
        
        def dfs(root):
            if(not root):
                return 
            queue = [(root,0)]
            while queue:
                node,depth = queue.pop(0)
                val_list = depth_dict.get(depth,[])
                val_list.append(node)
                depth_dict[depth] = val_list
                if(node.left):
                    queue.append((node.left,depth+1))
                if(node.right):
                    queue.append((node.right,depth+1))
        
        dfs(root)
        for key in depth_dict:
            
            curr_list = depth_dict[key]
            
            for i in range(len(curr_list)-1):
                
                curr_node = curr_list[i]
                next_node = curr_list[i+1]
                
                curr_node.next = next_node
                
        return root