# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = [[root]]
        paths = []
        
        prev_val = None
        while queue:
            node_list = queue.pop(0)
            node = node_list[-1]
            if(prev_val!=None):
                node.val = prev_val+1
                prev_val = prev_val+1
            else:
                node.val=1
                prev_val=1
            new_list = node_list[:]
            new_list2 = node_list[:]
            if(not node.left and not node.right):
                paths.append([node.val for node in new_list])
                continue
            if(node.left):
                new_list.append(node.left)
                queue.append(new_list)
            if(node.right):
                new_list2.append(node.right)
                queue.append(new_list2)
        
        if(len(paths)==1):
            return len(paths[0])-1
        print(paths)
        max_width = -1e9
        for i in range(len(paths)-1):
            for k in range(1,len(paths)):
                path1 = paths[i]
                path2 = paths[k]
                similar = False
                similar_count = 0
                for j in path1[1:]:
                    if j in path2:
                        similar = True
                        similar_count+=1
                    else:
                        break
                    
                if(similar):
                    max_width = max(max_width,len(path1)-1,len(path2)-1,len(path1)-1+len(path2)-1-(2*similar_count))
                else:
                    max_width = max(max_width,len(path1)-1 + len(path2)-1)
                    
        return max_width
                
                