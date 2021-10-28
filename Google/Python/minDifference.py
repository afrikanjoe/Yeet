"""
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

"""




class Solution:
    def minDifference(self, nums):
        if len(nums) < 4:
            return 0
        
        nums.sort()
        
        largest = nums[-1]
        second_largest = nums[-2]
        third_largest = nums[-3]
        fourth_largest = nums[-4]
        
        smallest = nums[0]
        second_smallest = nums[1]
        third_smallest = nums[2]
        fourth_smallest = nums[3]
        
        return min(largest-fourth_smallest, second_largest - third_smallest, third_largest-second_smallest, fourth_largest-smallest)
    
if __name__ == "__main__":
    nums = [5,3,2,4]
    print(Solution().minDifference(nums))
    nums = [1,5,0,10,14]
    print(Solution().minDifference(nums))
    nums = [6,6,0,1,1,4,6]
    print(Solution().minDifference(nums))
    nums = [1,5,6,14,15]
    print(Solution().minDifference(nums))