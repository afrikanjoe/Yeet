"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)-1
        if n==0:
            return
        j=n
        while nums[j-1]>=nums[j]:
            j-=1
            if j == 0:
                nums[:]=nums[::-1]
                return
        
        
        while nums[j-1]>=nums[n]:
            n-=1
        nums[n],nums[j-1]=nums[j-1],nums[n]
        nums[:]=nums[:j]+nums[j:][::-1]


if __name__ == "__main__":
    inp = [1,2,3,4,5,7,8,6]
    Solution().nextPermutation(inp)
    print(inp)
    inp = [1,3,2]
    Solution().nextPermutation(inp)
    print(inp)

    