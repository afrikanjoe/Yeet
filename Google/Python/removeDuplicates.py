"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums):
        place_index = 0 
        prev = None
        curr_index = 0 
        count  = 0 
        while curr_index< len(nums):
            
            val1 = nums[curr_index]
            if(val1==prev):
                pass
            else:
                nums[place_index] = val1
                place_index+=1
                prev = nums[curr_index]
                count+=1
            curr_index+=1
        return count


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))