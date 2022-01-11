"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

"""

class Solution:
    def maxSubArray(self, nums):
        
        max_sum = - 2**32
        curr_sum = 0
        for i in nums: 
            curr_sum += i
            if(curr_sum<=0):
                max_sum = max(curr_sum,max_sum)
                curr_sum = 0
            else:
                max_sum = max(curr_sum,max_sum)
        return max_sum 

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(Solution().maxSubArray(nums))