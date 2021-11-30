"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""

class Solution:
    def permute(self, nums):
        
        queue = [[i] for i in nums]
        res = []
        while queue:
            
            curr_list = queue.pop()
            added = False
            for i in nums:
                if(i not in curr_list):
                    new_list = curr_list[:]
                    new_list.append(i)
                    added = True
                    queue.append(new_list)
            if(not added):
                res.append(curr_list)
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))
