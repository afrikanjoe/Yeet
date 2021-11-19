"Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom."
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if(not root):
            return 
        depths = {}
        queue = [(root,0,0)]
        parents = {}
        
        while queue:
            
            node,depth,column = queue.pop(0)
            print(node.val,depth,column)
            val = depths.get(depth,[])
            val.append([depth,column,node.val])
            depths[depth] = val
            if(node.right):
                queue.append((node.right,depth+1,column+1))
                parents[node.right.val] = node.val
            if(node.left):
                queue.append((node.left,depth+1,column-1))
                parents[node.left.val] = node.val
            
        res = []
        for i in sorted(depths.keys()):
            ls = depths[i]
            print(ls)
            res.append(ls[0][-1])
        return res