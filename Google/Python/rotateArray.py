"""

Given an array, rotate the array to the right by k steps, where k is non-negative.


"""

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = [0]*len(nums)
        for i in range(len(nums)):
            new_nums[(i+k)%len(nums)] = nums[i]
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(Solution().rotate(nums,k))