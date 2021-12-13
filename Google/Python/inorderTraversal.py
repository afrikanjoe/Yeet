# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.itrav = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if(root):
                self.inorderTraversal(root.left)
                self.itrav.append(root.val)
                self.inorderTraversal(root.right)
        helper(root)
        return self.itrav

if __name__ == "__main__":
    