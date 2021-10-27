"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.


"""



class Solution:
    # Intuition here is correct
    # need to now do it sorting wise
    def minPairSum(self, nums):
        maxa = 0 
        while nums:
            val1 = min(nums)
            val2 = max(nums)
            suma = val1+val2
            nums.remove(val1)
            nums.remove(val2)
            maxa = max(suma,maxa)
        return maxa
    
    # same logic much faster
    def minPairSum(self, nums: List[int]) -> int:
        maxa = 0 
        nums = sorted(nums)
        end = len(nums)-1
        start = 0
        while start<end:
            val1 = nums[start]
            val2 = nums[end]
            suma = val1+val2
            maxa = max(suma,maxa)
            start+=1
            end-=1
        return maxa

if __name__=="__main__":
    nums = [3,5,2,3]
    print(Solution().minPairSum(nums))
    nums = [3,5,4,2,4,6]
    print(Solution().minPairSum(nums))