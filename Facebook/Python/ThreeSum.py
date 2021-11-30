"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

"""

class Solution:
    def threeSum(self, nums):
        if(len(nums)<3):
            return []
        res = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i==j):
                    continue
                curr_sum = nums[i]+nums[j]
                if(-curr_sum in nums and nums.index(-curr_sum)!=(j) and nums.index(-curr_sum)!=(i)):
                    triple = sorted([nums[i],nums[j],-curr_sum])
                    if(triple not in res):
                        res.append(triple)
        return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(Solution().threeSum(nums))