"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] 
might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    def search(self, nums, target):
        
        min_index = nums.index(min(nums))
        
        left = nums[0:min_index]
        right = nums[min_index:]
        return max(self.binary_search(left,target,0),self.binary_search(right,target,min_index))
        
    def binary_search(self,arr,target,start_index):
        start = 0 
        end = len(arr)-1
        res = -1
        while start<=end:
            
            mid = (start+end)>>1
            if(arr[mid]==target):
                res = mid +start_index
                break
            elif(arr[mid]<target):
                start=mid+1
            else:
                end = mid-1
        return res

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums,target))