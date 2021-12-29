"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsetsWithDup(self, nums):
        
        queue = [[(i,nums[i])] for i in range(len(nums))]
        
        visited = []
        while queue:
            
            ls = sorted(queue.pop(0))
            if ls not in visited:
                visited.append(ls)
            for i,val, in enumerate(nums):
                if((i,val) not in ls):
                    new_ls = ls[:] + [(i,val)]
                    queue.append(new_ls)
        
        ans = [[]]
        for s in visited:
            s_true  = []
            for tup in s:
                s_true.append(tup[1])
                
            s_true = sorted(s_true)
            if(s_true not in ans):
                ans.append(s_true)
        return ans
            
if __name__ == "__main__":
    nums = [4,4,4,1,4]
    print(Solution().subsetsWithDup(nums))