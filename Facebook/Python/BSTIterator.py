# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.traversal =[]
        self.index = 0
        self.in_order(root)
    
    def in_order(self,root):
        if(root.left):
            self.in_order(root.left)
        self.traversal.append(root.val)
        if(root.right):
            self.in_order(root.right)
        
        
        

    def next(self) -> int:
        val = self.traversal[self.index]
        self.index+=1
        return val
        

    def hasNext(self) -> bool:
        return self.index<len(self.traversal)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()