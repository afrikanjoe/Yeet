"""

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
"""



class Solution:
    def findLengthOfLCIS(self, nums):
        max_len = 0
        temp =  []
        for i in range(len(nums)):
            if(temp):
                if(nums[i]>temp[-1]):
                    temp.append(nums[i])
                else:
                    max_len= max(max_len,len(temp))
                    temp = [nums[i]]
            else:
                temp.append(nums[i])
        max_len= max(max_len,len(temp))
        return max_len


if __name__ == "__main__":
    inp = [1,2,3,4,5,1,2,3,4,5,6,1,2,3]
    print(Solution().findLengthOfLCIS(inp))