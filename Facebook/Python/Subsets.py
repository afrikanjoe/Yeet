"""

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self,nums):
        
        visited = []
        queue = [[]]
        while queue:
            curr_list = queue.pop()
            visited.append(curr_list)
            for i in nums:
                new_list = curr_list[:]
                if(i not in curr_list):
                    new_list  = sorted(new_list + [i]) 
                if(new_list not in visited):
                    queue.append(new_list)
        return visited

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))
    nums = [1,2,3,4]
    print(Solution().subsets(nums))