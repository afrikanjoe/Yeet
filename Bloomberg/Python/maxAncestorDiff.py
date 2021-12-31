"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where 
v = |a.val - b.val| and a is an ancestor of b.
A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq
class Solution:
    def maxAncestorDiff(self, root):
        
        heap = []
        
        def helper(root,parent_list):
            
            if(not root):
                pass
            else:
                
                for i in parent_list:
                    
                    heapq.heappush(heap,-abs(root.val-i))
                new_list = parent_list[:]+[root.val]
                helper(root.left,new_list)
                helper(root.right,new_list)
            
        helper(root,[])
        if(heap):
            return -heap[0]
        else:
            return 0

# function for constructing trees
def constructTree(tree):
    tree_list = tree[:]
    for i,val in enumerate(tree_list):
        if(val!=None):
            tree_list[i] = TreeNode(val)

    curr_node_index = 0 
    children = 1

    while children<len(tree_list):
        curr_node = tree_list[curr_node_index]

        if(curr_node==None):
            curr_node_index+=1
            continue

        child_1 = tree_list[children]
        children+=1
        if(children<len(tree_list)):
            child_2 = tree_list[children] 
            children+=1
        else:
            child_2 = None

        curr_node.left = child_1
        curr_node.right = child_2
        curr_node_index+=1
    return tree_list[0]



def bfs(root):
    queue =[root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if(node.left):
            queue.append(node.left)
        if(node.right):
            queue.append(node.right)
    

    






if __name__ == "__main__":
    tree= [8,3,10,1,6,None,14,None,None,4,7,13]
    root = constructTree(tree)
    print(Solution().maxAncestorDiff(root))

    tree2 = [1,None,2,None,0,3]
    root = constructTree(tree2)
    print(Solution().maxAncestorDiff(root))
        
        
        
        
        