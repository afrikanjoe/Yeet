# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = []
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root,num):
            if(not root.left and not root.right):
                self.nums.append(int(num+str(root.val)))
            
            if(root.left):
                helper(root.left,num+str(root.val))
            if(root.right):
                helper(root.right,num+str(root.val))
        helper(root,"")
        return sum(self.nums)