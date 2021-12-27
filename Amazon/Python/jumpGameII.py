"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""

from functools import lru_cache
class Solution:
    def jump(self, nums):
        
        counts = []
        @lru_cache(maxsize=None)
        def helper(nums,i,count):
            if(i==len(nums)-1):
                counts.append(count)
            else:
                for j in range(nums[i],0,-1):
                    if(i+j)<len(nums):
                        new_count = helper(nums,i+j,count+1)
        
        helper(tuple(nums),0,0)
        return min(counts)

class OptimalSolution:
     def jump(self, nums: List[int]) -> int:
            jumps = 0
            current_jump_end = 0
            farthest = 0
            for i in range(len(nums) - 1):
                # we continuously find the how far we can reach in the current jump
                farthest = max(farthest, i + nums[i])
                # if we have come to the end of the current jump,
                # we need to make another jump
                if i == current_jump_end:
                    jumps += 1
                    current_jump_end = farthest
            return jumps

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().jump(nums))
    nums = [2,1]
    print(Solution().jump(nums))