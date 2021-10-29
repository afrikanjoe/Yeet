"""
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = [root]
        ans = {}
        parents = {}
        remove_root = False
        
        while queue:    
            node = queue.pop(0)    
            if(node.left):
                queue.append(node.left)
                parents[node.left.val] = node
            if(node.right):
                queue.append(node.right)
                parents[node.right.val] = node
        
        
        for i in to_delete:
            if(i==root.val):
                remove_root = True
                node = root
            else:
                node = self.remove_left_right(parents[i],i)
            if(node.left):
                ans[node.left.val] = node.left
            if(node.right):
                ans[node.right.val] = node.right
                
            if(i in ans.keys()):
                tmp = ans[i]
                del ans[i]
                if(tmp.right):
                    ans[tmp.right.val] = tmp.right
                if(tmp.left):
                    ans[tmp.left.val] = tmp.left
        if(not remove_root):      
            for i in parents.keys():
                if(parents[i].val==root.val):
                    ans[-1]=root
                    break
            
        return list(ans.values())
                
        
    def remove_left_right(self,parent,val):
        tmp = None
        if(parent.left and parent.left.val == val):
            tmp = parent.left
            parent.left = None
        else:
            tmp = parent.right
            parent.right=None 
        return tmp
            
            