# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root):
        
        paths = []
        def longestConsecutive(root,curr_list):
            if(not root):
                if(curr_list and curr_list not in paths):
                    paths.append(curr_list)
            else:
                if(not curr_list or (root.val-curr_list[-1])!=1):
                    if(curr_list and curr_list not in paths):
                        paths.append(curr_list)
                    new_list = [root.val]
                else:
                    new_list = curr_list +[root.val]
                longestConsecutive(root.left,new_list)
                longestConsecutive(root.right,new_list)             
        
        longestConsecutive(root,[])
        longest_consec = 0 
        for i in paths:
            longest_consec = max(len(i),longest_consec)
        return longest_consec
        