"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue for doing bfs
        queue = [root]
        parent_dict = {}
        # temporary dict that will store current leaves
        leaves = []
        leaves_val = []
        # list that will return the answer
        return_list = []
        node_list = []
        while queue:
            node = queue.pop()
            if(node): 
                node_list.append(node.val)
            if(node.left): 
                queue.append(node.left)
                parent_dict[node.left.val] = node
            if(node.right):
                queue.append(node.right)
                parent_dict[node.right.val] = node
            # check if it’s a leaf
            if ((not node.left) and (not node.right)):
                leaves.append(node)
                leaves_val.append(node.val)
       
        # add this first list of leaves to the current list of nodes
        return_list.append(leaves_val)
        
        while len(node_list)>1:
            curr_leaves = []
            curr_leaves_val = []
            while leaves: 
                node = leaves.pop(0)
                node_list.remove(node.val)
                parent = parent_dict[node.val]
                if(parent.left == node):
                    parent.left = None
                elif(parent.right == node):
                    parent.right = None
                if(not parent.right and not parent.left):
                    curr_leaves.append(parent)
                    curr_leaves_val.append(parent.val)
            return_list.append(curr_leaves_val)
            leaves = curr_leaves[:]
        return return_list
