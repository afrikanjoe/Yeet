class Solution:
    @staticmethod
    def searchInsert(nums, target):
        low = 0
        high = len(nums)-1
        while (low<high):
            mid = low + high >>1 
            if(nums[mid]<target):
                low = mid+1
            elif(nums[mid]==target):
                return mid
            else:
                high = mid
        if(target>nums[low]):
            low+=1
        return low


if __name__=="__main__":
    inp = [1,3,5,6]
    target = 2
    print(Solution.searchInsert(inp,target))
