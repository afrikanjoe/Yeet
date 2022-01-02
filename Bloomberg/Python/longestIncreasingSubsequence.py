"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""


class Solution:
    def lengthOfLIS(self, nums):
        
        lis = [1] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(0,i):
                
                if(nums[j]<nums[i]):
                    
                    lis[i] = max(lis[i],lis[j]+1)
        return max(lis)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))