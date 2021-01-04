"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


"""

class Solution:
    def missingNumberBruteForce(self, nums):
        count = {}
        for i  in nums:
            count[i] = 1
        for i in range(0,len(nums)+1):
            if(count.get(i,0)==0):
                return i

    def missingNumber(self, nums):
        ans = len(nums)*((len(nums)+1)/2)
        for i in range(len(nums)):
            print(i)
            ans-=nums[i]
        return int(ans)




if __name__=="__main__":

    inp = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    print("Brute Force:",sol.missingNumberBruteForce(inp))
    print(sol.missingNumber(inp))