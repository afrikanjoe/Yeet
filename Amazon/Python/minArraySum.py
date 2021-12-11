"""

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target, nums):
        
        queue = [([i],val) for i,val in enumerate(nums)]
        while queue:
            tup_list,val = queue.pop(0)
            if(val>=target):
                return len(tup_list)
            for i,val2 in enumerate(nums):
                diff = (i-tup_list[-1])
                if(i not in tup_list and diff==1):
                    new_list = tup_list[:]+ [i]
                    new_val = val+val2
                    queue.append((new_list,new_val))
        return 0

if __name__ == "__main__":
    target = 213
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    print(Solution().minSubArrayLen(target,nums))
        