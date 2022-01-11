from functools import lru_cache
class Solution:
    def rob(self, nums):
       
        @lru_cache(maxsize=None)
        def rob_helper(index,money):
            
            if(index>=len(nums)):
                return money 
            else:
                return max(rob_helper(index+2,money+nums[index]),rob_helper(index+1,money))
        
        if(len(nums)==0):
            return 0 
        elif(len(nums)==1):
            return nums[0]
        elif(len(nums)==2):
            return max(nums)
        else:
            return rob_helper(0,0)

if __name__ == "__main__":
    nums = [2,7,9,3,1,21]
    print(Solution().rob(nums))