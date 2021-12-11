"""
Given an array of integers nums and an integer k, 
return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if(k<=1):
            return 0
        count = 0 
        for i in range(1,len(nums)+1):
            for j in range(0,len(nums)-i+1):
                if(self.compute_product(nums[j:i+j],k)):
                    count+=1
        return count 
            
    def compute_product(self,nums,k):
        mult = 1
        for i in nums:
            mult*=i
            if(mult>=k):
                return False
        return True


if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums,k))