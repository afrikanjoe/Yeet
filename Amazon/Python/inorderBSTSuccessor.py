# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
class Solution:
    def __init__(self):
        self.inorder_heap = []
    
    def inorderSuccessor(self, root, p):
        
        def helper(root,p):
            if(root):
                if(root.val>p.val):
                    heapq.heappush(self.inorder_heap,(root.val,root))
                helper(root.left,p)
                helper(root.right,p)
        
        helper(root,p)
        
        if(len(self.inorder_heap)>0):
            return heapq.heappop(self.inorder_heap)[1]