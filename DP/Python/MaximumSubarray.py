"""
Divide and Conquer Solution: https://www.youtube.com/watch?v=yBCzO0FpsVc

"""

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
    @staticmethod
    def crossing_sum(mid,nums):
        index_left = mid
        index_right = mid
        sum_left = nums[index_left]
        sum_right = nums[index_right+1]
        max_left = sum_left
        max_right = sum_right 
        for i in range(index_left-1,-1,-1):
            temp_sum = sum_left + nums[i]
            #print(temp_sum,max_left)
            if(temp_sum>max_left):
                index_left = i
                max_left = temp_sum
            sum_left= temp_sum

        for i in range(index_right+1,len(nums)):
            temp_sum = sum_right + nums[i]
            #print(temp_sum,max_right)
            if(temp_sum>max_right):
                index_right = i
                max_right = temp_sum
            sum_right= temp_sum

        return index_left,index_right



    @staticmethod
    def maxSubArrayDNC(nums):
        left=0
        right=len(nums)-1
        if(left==right):
            return nums[left]
        if(right<0):
            return "Empty Array"

        mid=(left+right)>>1
        
        left_sum = Solution.maxSubArrayDNC(nums[0:mid+1])
        right_sum = Solution.maxSubArrayDNC(nums[mid+1:])
        cl, cr = Solution.crossing_sum(mid,nums)
        center_sum = sum(nums[cl:cr+1])
        return max(left_sum,right_sum,center_sum)
    


if __name__=="__main__":
    inp = [-2,1,-3,4,-1,2,1,-5,4]
    inp2 = [-1,3,4,-5,9,-2]
    inp3 = [1,2]
    inp4 = [-1,0,-2]
    inp5 = [-1,-2,-3,0]
    print(Solution.maxSubArray(inp))
    print(Solution.maxSubArray(inp2))
    print(Solution.maxSubArray(inp3))
    print(Solution.maxSubArray(inp4))
    print(Solution.maxSubArray(inp5))
    print("-----DNC------Solutions----")
    print(Solution.maxSubArrayDNC(inp))
    print(Solution.maxSubArrayDNC(inp2))
    print(Solution.maxSubArrayDNC(inp3))
    print(Solution.maxSubArrayDNC(inp4))
    print(Solution.maxSubArrayDNC(inp5))