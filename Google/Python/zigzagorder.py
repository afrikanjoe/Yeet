"""

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        depth_dict = {}
        
        def dfs(root):
            if(not root):
                return 
            queue = [(root,0)]
            while queue:
                node,depth = queue.pop(0)
                val_list = depth_dict.get(depth,[])
                val_list.append(node.val)
                depth_dict[depth] = val_list
                if(node.left):
                    queue.append((node.left,depth+1))
                if(node.right):
                    queue.append((node.right,depth+1))
        
        dfs(root)
        ans = []
        for key in depth_dict.keys():
            if key%2==0:
                ans.append(depth_dict[key])
            else:
                ans.append(depth_dict[key][::-1])
        return ans
            