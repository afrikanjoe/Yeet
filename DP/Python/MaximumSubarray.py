class Solution:
    @staticmethod
    def maxSubArray(nums):
        if(len(nums)==0):
            return 0
        best = nums[0]
        ssum=nums[0]
        for i in range(1,len(nums)):
            ssum = nums[i]+ssum
            ssum = max(nums[i],ssum)
            best = max(best,ssum)
            
        return best


if __name__=="__main__":
    inp = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution.maxSubArray(inp))