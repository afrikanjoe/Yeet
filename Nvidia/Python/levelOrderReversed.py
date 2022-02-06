# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        levels_dict = {}
        queue = [(0,root)]
        if(not root):
            return []
        while queue: 
            
            depth,node = queue.pop(0)
            val = levels_dict.get(depth,[])
            val.append(node.val)
            levels_dict[depth] = val
            if(node.left):
                queue.append((depth+1,node.left))
            if(node.right):
                queue.append((depth+1,node.right))
                
        ans = list(levels_dict.values())
        return ans[::-1]
        