"""Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight
 without alerting the police."""
class Solution:
    def rob(self, nums):
        
        queue = [[i] for i in range(min(len(nums),2))]
        res = []
        while queue:
            
            curr_list = queue.pop()
            last_index = curr_list[-1]
            added = False
            for i in range(last_index+1,len(nums)):
                
                new_list = curr_list[:]
                if(i-last_index>1):
                    new_list.append(i)
                    queue.append(new_list)
                    added = True
            if(not added):
                res.append(curr_list)
        
        max_sum = 0 
        for ls in res:
            curr_sum = 0
            for index in ls:
                curr_sum+=nums[index]
            max_sum = max(curr_sum,max_sum)
            
        return max_sum

from functools import lru_cache
class SolutionOptimal:
    def rob(self, nums):
       
        @lru_cache(maxsize=None)
        def rob_helper(i,nums):
            
            if(i>=len(nums)):
                return 0 
            else:
                return max(rob_helper(i+2,nums)+nums[i],rob_helper(i+1,nums))
            
        if(len(nums)==1):
            return nums[0]
        elif(len(nums)==2):
            return max(nums)
        else:
            return rob_helper(0,tuple(nums))

if __name__ == "__main__":
    nums = [2,7,9,3,1]
    print(SolutionOptimal().rob(nums))
            
            
                
        