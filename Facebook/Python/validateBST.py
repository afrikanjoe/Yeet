"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

When I tell you this problem defeated me...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True

        def isvalidhelper(root,low=-2**32,high=2**32):
            if(not root):
                return True
            
            if(root.val<=low or root.val>=high):
                return False
            return isvalidhelper(root.left,low,root.val) and isvalidhelper(root.right,root.val,high)
        return isvalidhelper(root)