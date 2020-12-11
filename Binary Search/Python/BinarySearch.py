"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, otherwise return -1.
"""


class Solution:
    @staticmethod
    def search(nums, target):
        start = 0
        end  = len(nums)-1
        ret = -1
        while(start<=end):
            mid = int((start + end)/2)
            if(nums[mid]==target):
                return mid
            elif (nums[mid]>target):
                end = mid-1
            else:
                start = mid+1
        return ret


if __name__ == "__main__":

    # Test case # 1
    nums = [-1,0,3,5,9,12] 
    target = 9
    print(Solution.search(nums,target))
    # Test case # 2
    nums = [-1,0,3,5,9,12] 
    target = 2
    print(Solution.search(nums,target))