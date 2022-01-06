"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

"""

class Solution:
    def threeSumClosest(self, nums, target):
        
        nums = sorted(nums)
        diff = 2**32
        val = None
        
        for i in range(0,len(nums)):
            
            first = nums[i]
            low = i+1
            high =  len(nums)-1
            
            while low<high:
                curr_sum = first + nums[low]+nums[high]
                
                if abs(curr_sum-target)<diff:
                    diff = abs(curr_sum-target)
                    val = curr_sum
                if(curr_sum>=target):
                    high-=1
                elif(curr_sum<target):
                    low+=1
        return val


if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    print(Solution().threeSumClosest(nums,target))