import sys
mini = -sys.maxsize - 1
class Solution:
    @staticmethod
    def findPeakElementBF(nums):
        index = 0 
        maxi = mini
        for i in range(len(nums)):
            if(nums[i]>maxi):
                index = i
                maxi  = nums[i]
        return index

    # This binary trick is actually crazy
    @staticmethod
    def findPeakElement(nums):
        low = 0
        high = len(nums)-1
        while(low<high):
            mid = int((low + high)>>1)
            val = nums[mid]
            if (val > nums[mid + 1]):
                high = mid 
            else:
                low = mid + 1
        return low
            


if __name__=="__main__":
    inp = [1,2,3,1]
    print(Solution.findPeakElementBF(inp))
    print(Solution.findPeakElement(inp))
        