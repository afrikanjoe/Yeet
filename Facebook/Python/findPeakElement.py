"""

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

class Solution:
    def findPeakElement(self, nums):
        min_val = -2**31
        index = None
        if(len(nums)<=2):
            return nums.index(max(nums))
        else:
            for i in range(1,len(nums)-1):
                val1 = nums[i-1]
                val2 = nums[i]
                val3 = nums[i+1]
                if(val2>val1 and val2>val3):
                    if(val2>min_val):
                        index = i
                        min_val = val2
            if(not index):
                return nums.index(max(nums))
            return index


if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    print(Solution().findPeakElement(nums))
