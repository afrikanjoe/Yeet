class Solution:
    def findMinClose(self, nums):
        start = 0
        end = len(nums)-1
        while(start<end):
            mid = start+end >>1
            if(nums[mid]>nums[mid+1]):
                start = mid +1
            else:
                end = mid
        return min(nums[start],nums[-1])

    def findMin(self,nums):
        start = 0
        end = len(nums)-1
        if(nums[end]>=nums[start]):
            return nums[0]

        while(start<end):
            mid = start+end >>1
            if(nums[mid]>nums[mid+1]):
                return nums[mid+1]
            if(nums[mid-1]>nums[mid]):
                return nums[mid]
            if(nums[mid]>nums[0]):
                start = mid + 1
            else:
                end = mid -1
            

        

        


if __name__=='__main__':
    inp = [3,4,5,1,2]
    inp2 = [1,2,3,4,5]
    inp3 = [4,5,6,7,0,1,2]
    inp4 = [0,1,2,4,5,6,7]
    inp5 = [3,1,2]
    inp6 = [2,3,4,5,1]
    inp7 = [3,4,5,6,1,2]
    print(Solution().findMinClose(inp))
    print(Solution().findMinClose(inp2))
    print(Solution().findMinClose(inp3))
    print(Solution().findMinClose(inp4))
    print(Solution().findMinClose(inp5))
    print(Solution().findMinClose(inp6))
    print(Solution().findMinClose(inp7))

    print('------------------------')
    print(Solution().findMin(inp))
    print(Solution().findMin(inp2))
    print(Solution().findMin(inp3))
    print(Solution().findMin(inp4))
    print(Solution().findMin(inp5))
    print(Solution().findMin(inp7))