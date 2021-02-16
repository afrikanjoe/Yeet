"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""



class Solution:
    def minSubArrayLen(self, target, nums):
        for i in range(1,len(nums)+1):
            for j in range(len(nums)):
                arr = nums[j:j+i]
                if(len(arr)==i):
                    if(sum(arr)>=target):
                        return(len(arr))
        return 0



if __name__=="__main__":
    tar = 15
    inp = [1,2,3,4,5]
    print(Solution().minSubArrayLen(tar,inp))