"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums):
        
        
        sums = sum(nums)
        n = len(nums)
        real_sum = (n*(n+1)/2)
        
        if 0 not in nums:
            return 0 
        else:
            return int(real_sum) - sums

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(nums))
        