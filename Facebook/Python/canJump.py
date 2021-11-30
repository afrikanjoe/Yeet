"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""

class Solution:
    def canJump(self, nums):
        m = len(nums)
        if not nums:
            return False
        
        queue = [[(0,nums[0])]]
        
        while queue:
            curr_list = queue.pop()
            last_step = curr_list[-1]
            index = last_step[0]
            reach = last_step[1]
            if(index+reach>=(len(nums)-1)):
                return True
            else:
                for i in range(reach,0,-1):
                    new_list = curr_list[:]
                    new_index = i+index
                    if(new_index<m):
                        tup = (new_index,nums[new_index])
                        new_list.append(tup)
                        queue.append(new_list)
        return False


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))