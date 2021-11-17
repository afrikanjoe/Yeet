"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.

This was one of my interview questions
"""

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.depth_sum_helper(nestedList,1)
        
    def depth_sum_helper(self,nestedList,depth):
        curr_sum = 0 
        for i in nestedList:
            if(not i.isInteger()):
                curr_sum = curr_sum + self.depth_sum_helper(i.getList(),depth+1)
            else:
                curr_sum= curr_sum + (depth * i.getInteger())
        return curr_sum
        