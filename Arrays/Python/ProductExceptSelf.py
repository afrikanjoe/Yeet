"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] 
is equal to the product of all the elements of nums except nums[i].
"""





class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        tmp =1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * tmp
            tmp *= nums[j]
        return res


if __name__=='__main__':
    inp =  [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(inp))