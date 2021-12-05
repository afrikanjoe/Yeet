"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
"""

class Solution:
    def findDuplicateBF(self, nums):
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i==j):
                    continue
                else:
                    if(nums[i]==nums[j]):
                        return nums[i]

    def findDuplicateNegativeMarking(self, nums):
        
        for i in range(len(nums)):        
            if(nums[abs(nums[i])]<0):
                return abs(nums[i])
            else:
                nums[abs(nums[i])]*=-1


    def findDuplicate(self, nums):
        
        
        ### If you have never seen this before it won't make sense
        ### This is floyd's hare a tortoise problem 
        
        # Phase I 
        tortoise = hare = nums[0]
        while True:
            
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if(hare == tortoise):
                break 
            
        # Phase II
        tortoise = nums[0]
        while tortoise!=hare:
            
            tortoise = nums[tortoise]
            hare = nums[hare]
            
            if(tortoise==hare):
                return hare
            
        return hare
            

if __name__ == "__main__":
    inp1 = [2,5,9,6,9,3,8,9,7,1]
    print(Solution().findDuplicate(inp1))
    inp2 = [3,1,3,4,2]
    print(Solution().findDuplicate(inp2))
