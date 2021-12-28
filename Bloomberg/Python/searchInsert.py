"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""



class Solution:
    def searchInsert(self, nums, target):
        
        low = 0 
        high = len(nums)-1
        
        while low<high:
            mid = (low+ high)>>1
            if(nums[mid]>=target):
                high = mid-1
            else:
                low = mid+1
                
        if(nums[low]>=target):
            return low
        else:
            return low+1

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums,target))