"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        queue = [root]
        node_dict = {}
        duplicate_subtrees = []
        leaf_duplicate = []
        while queue:
            node_curr = queue.pop(0)
            if(node_curr.left):
                queue.append(node_curr.left)
            if(node_curr.right):
                queue.append(node_curr.right)
            
            dict_val = node_dict.get(node_curr.val,0)
            if(dict_val):
                ls1 = self.dfs(dict_val)
                ls2 = self.dfs(node_curr)
                if(ls1 == ls2):
                    if(node_curr.val not in leaf_duplicate or len(ls1)>1):
                        duplicate_subtrees.append(node_curr)
                    if(len(ls1)==1):
                        leaf_duplicate.append(node_curr.val)
            node_dict[node_curr.val] = node_curr
        return duplicate_subtrees
        
            
    def dfs(self,root):
        node_list = []
        queue = [root]
        while queue:
            node_curr = queue.pop(0)
            if(node_curr.left):
                queue.append(node_curr.left)
            if(node_curr.right):
                queue.append(node_curr.right)
            node_list.append(node_curr.val)
        return node_list