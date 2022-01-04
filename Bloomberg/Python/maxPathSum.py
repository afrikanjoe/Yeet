# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
         self.max_sum = -2**32
    def maxPathSum(self, root):
        self.helper(root)
        return self.max_sum
        
    
    def helper(self,root):
        if(not root):
                return 0
        else:
            left_subtree_max = max(self.helper(root.left),0) 
            right_subtree_max = max(self.helper(root.right),0)
                
            new_path = root.val + left_subtree_max + right_subtree_max
                
                
            self.max_sum = max(new_path,self.max_sum)
            
            # This is the split condition, comparie the right and left subtree 
            return root.val + max(left_subtree_max,right_subtree_max)