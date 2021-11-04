"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p, q):
        parent_dictionary = {}
        node_dict = {}
        queue = [p,q]
        while queue:
            node = queue.pop()
            node_dict[node.val] = node
            if(not node.parent): # this check is purely for the root
                parent_dictionary[node.val] = None
            else:
                parent_dictionary[node.val] = node.parent.val

            if(node.parent):
                queue.append(node.parent)

           
    
        p_ancestors = [p.val] 
        q_ancestors = [q.val]
        parent = p.val
        while parent!=None:
            new_parent = parent_dictionary.get(parent,None)
            if(new_parent!=None):
                p_ancestors.append(new_parent)
            parent = new_parent

        parent = q.val
        while parent!=None:
            new_parent = parent_dictionary.get(parent,None)
            if(new_parent!=None):
                q_ancestors.append(new_parent)
            parent = new_parent
            
        for i in p_ancestors:
            if i in q_ancestors:
                return node_dict[i] 

        if q.val in p_ancestors:
            return node_dict[p]
        else:
            return node_dict[q] 


