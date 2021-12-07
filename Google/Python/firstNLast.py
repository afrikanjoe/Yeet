"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""



class Solution:
    
    def __init__(self):
        self.indices = []
    def searchRange(self, nums, target):
        
        self.helper(nums,0,len(nums)-1,target)
        if(self.indices):
            return [min(self.indices),max(self.indices)]
        else:
            return [-1,-1]
                
    
    def helper(self,nums,start,end,target):
        
        if(start<=end):
            mid = (start+end)>>1
            if(nums[mid]==target):
                self.indices.append(mid)
                self.helper(nums,start,mid-1,target)
                self.helper(nums,mid+1,end,target)
            elif(nums[mid]>target):
                self.helper(nums,start,mid-1,target)
            else:
                self.helper(nums,mid+1,end,target)



if __name__ == "__main__":
    nums = [5,7,7,8,8,8,10]
    target = 8
    print(Solution().searchRange(nums,target))