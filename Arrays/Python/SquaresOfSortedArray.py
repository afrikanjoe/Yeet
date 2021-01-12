"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""
import math
class Solution:
    def sortedSquares(self, nums):
        
        res = [0]*len(nums)
        start = 0 
        end = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if(abs(nums[start])>abs(nums[end])):
                res[i] = nums[start]**2
                start+=1
            else:
                res[i] = nums[end]**2
                end-=1
        return res



        
        



if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    nums1 = [-7,-3,2,3,11]
    print(Solution().sortedSquares(nums))
    print(Solution().sortedSquares(nums1))

