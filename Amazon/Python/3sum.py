"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    def threeSum(self, nums):
        sols = []
        val_dict = {}
        for i in range(len(nums)):
            
            val = val_dict.get(nums[i],[])
            val.append(i)
            val_dict[nums[i]]= val
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i==j):
                    continue
                else:
                    
                    curr_sum = nums[i]+ nums[j]
                    vals = val_dict.get(-curr_sum,[])
                    for index in vals:
                        
                        if(index!=i and index!=j):
                            
                            triple = sorted([nums[i],nums[j],-curr_sum])
                            if(triple not in sols):
                                sols.append(triple)
        return sols


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))