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
                for node in dict_val:
                    if(self.dfs2(node,node_curr)):
                        if(not node_curr.left and not node_curr.right):
                            if(node_curr.val not in leaf_duplicate):
                                duplicate_subtrees.append(node_curr)
                                leaf_duplicate.append(node_curr.val)
                        else:
                            duplicate_subtrees.append(node_curr)
                            
                        
            if(dict_val):
                new_list = dict_val[:]
                new_list.append(node_curr)
                node_dict[node_curr.val] = new_list
            else:
                node_dict[node_curr.val] = [node_curr]
        return duplicate_subtrees
        
    def dfs2(self,root,root2):
        queue = [root]
        queue2 = [root2]
        while queue and queue2:
            node_curr = queue.pop(0)
            node_curr2 =  queue2.pop(0)
            if(node_curr.val!=node_curr2.val):
                return False
            if(not node_curr.left and node_curr2.left):
                return False
            if(not node_curr.right and node_curr2.right):
                return False
            
            # first subtree
            if(node_curr.left):
                queue.append(node_curr.left)
            if(node_curr.right):
                queue.append(node_curr.right)
            
            # second subtree
            if(node_curr2.left):
                queue2.append(node_curr2.left)
            if(node_curr2.right):
                queue2.append(node_curr2.right)
                
       
        if(len(queue2)>0 or len(queue)>0):
            return False
        #print(root,root2)
        return True
    
    def dfs(self,root):
        node_list = []
        queue = [root]
        while queue :
            node_curr = queue.pop(0)
            if(node_curr.left):
                queue.append(node_curr.left)
            if(node_curr.right):
                queue.append(node_curr.right)
            node_list.append(node_curr.val)
        return node_list
            
            
    