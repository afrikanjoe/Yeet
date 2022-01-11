"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

"""

from functools import lru_cache
class Solution:
    def rob(self, nums):
        
        @lru_cache(None)
        def rob_helper(index,money,first_house):
            
            if(index>=len(nums)):
                return money
            else:
                if(index==0):
                    return max(rob_helper(index+1,money,False),rob_helper(index+2,money+nums[index],True))
                elif(first_house and index==(len(nums)-1)):
                    return money
                else:
                    return max(rob_helper(index+1,money,first_house),rob_helper(index+2,money+nums[index],first_house))
                    
        if(len(nums)==0):
            return 0 
        elif(len(nums)>0 and len(nums)<2):
            return max(nums)
        else:
            return rob_helper(0,0,False)


if __name__ == "__main__":
    nums = [2,3,2]
    print(Solution().rob_helper(nums))
    nums = [1,2,3,1]
    print(Solution().rob_helper(nums))