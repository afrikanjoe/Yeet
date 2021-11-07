"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. 
There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def __init__(self):
        self.results_dict = {}
        
    def dfs_helper(self,root,column,depth):
        if(root):
            result_list = self.results_dict.get(column,0)
            if(result_list == 0 ):
                self.results_dict[column] = [(depth,root.val)]
            else:
                result_list.append((depth,root.val))
            self.dfs_helper(root.left,column-1,depth+1)
            self.dfs_helper(root.right,column+1,depth+1)
            
            
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs_helper(root,0,0)
        keys = sorted(list(self.results_dict.keys()))
        res = []
        for key in keys:
            order = sorted(self.results_dict[key])
            res.append([num[1] for num in order])
        return res
        