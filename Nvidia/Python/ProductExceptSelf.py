from collections import Counter
class Solution:
    def productExceptSelf(self, nums):
        c = Counter(nums)
        zero_count = c.get(0,0)
        if(zero_count>1):
            return [0]*len(nums)
        elif(zero_count==1):
            
            mult = 1
            for i in nums:
                if(i!=0):
                    mult*=i
            ans = [0]*len(nums)
            index = nums.index(0)
            ans[index] = mult
            return ans
        else:
            mult = 1
            for i in nums:
                mult*=i
            
            for i in range(len(nums)):
                nums[i] = int(mult/nums[i])
            return nums

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums))

    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))
    
    nums = [1,2,3,4,0,0]
    print(Solution().productExceptSelf(nums))