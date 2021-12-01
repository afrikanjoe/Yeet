"""
One way of balancing the tree lol.
"""



class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        if(not root):
            return 
        count = 0 
        node_dict = {}
        queue = [root]
        
        while queue:
            
            curr_node = queue.pop(0)
            node_dict[count] = TreeNode(curr_node.val)
            count+=1
            if(curr_node.left):
                queue.append(curr_node.left)
            
            if(curr_node.right):
                queue.append(curr_node.right)
        
        count = 0 
        root = node_dict[count]
        for i in list(node_dict.keys())[1:]:
            new_node = node_dict[i]
            if(not root.left):
                root.left = new_node
            elif(not root.right):
                root.right = new_node
            else:
                count+=1
                root = node_dict[count]
                root.left = new_node
        return node_dict[0]