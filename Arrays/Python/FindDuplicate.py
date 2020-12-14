"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

    How can we prove that at least one duplicate number must exist in nums? 
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n2)?

"""


class Solution:
    @staticmethod
    def findDuplicate(nums):
        pass
    @staticmethod    
    def prove_duplicate(nums):
        return not (len(nums) == len(set(nums)))
    @staticmethod
    def findDuplicateDict(nums):
        count_dict = {}
        res = None
        for  i in nums:
            count_dict[i] = count_dict.get(i,0)+1
            if(count_dict[i])>1:
                res = i 
                break
        return res

    @staticmethod
    def findDuplicateBest(nums):
        # if there are duplicates it will get mapped to 
        # the same index twice
        for i in nums:
            if(nums[abs(i)-1]<0):
                return i 
            nums[abs(i)-1] = - nums[abs(i)-1]

if __name__=="__main__":
    inp = [1,3,4,2,2]
    print("Are there duplicates?")
    print(Solution.prove_duplicate(inp))
    print("Can you solve the problem without modifying the array nums? Yes")
    print(Solution.findDuplicateDict(inp))
    print("Constant Space O(n)")
    print(Solution.findDuplicateBest(inp))