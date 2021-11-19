"""

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""

class Solution:
    def verticalOrderClose(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        cols = {}
        res = []
        def dfs(root,col):
            print(root.val)
            clist = cols.get(col,[])
            if(len(clist)>0):
                clist.append(root.val)
                cols[col] = clist
            else:
                cols[col] = [root.val]
            if(root.left):
                dfs(root.left,col-1)
            if(root.right):
                dfs(root.right,col+1)
        dfs(root,0)
        for i in sorted(list(cols.keys())):
            res.append(cols[i])
        return res

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        cols = {}
        res = []
        queue = [(root,0)]
        while queue:
            node,col = queue.pop(0)
            clist = cols.get(col,[])
            if(len(clist)>0):
                clist.append(node.val)
                cols[col] = clist
            else:
                cols[col] = [node.val]
            if(node.left):
                queue.append((node.left,col-1))
            if(node.right):
                queue.append((node.right,col+1))
        for i in sorted(list(cols.keys())):
            res.append(cols[i])
        return res