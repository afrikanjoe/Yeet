"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""

class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        queue = []
        zero_count = 0
        prev = None
        # initialize intial guesses
        for i in range(len(nums)):
            val = nums[i]
            if(val==0 and prev==0):
                return True
            queue.append((i,i,val))
            prev= val
        visited = []    
        while queue:
            node_tup = queue.pop()
            visited.append(node_tup)
            if(node_tup[0]-1>=0):
                new_val = node_tup[-1] + nums[node_tup[0]-1] 
                if(new_val%k==0):
                    return True
                else:
                    new_tup = (node_tup[0]-1,node_tup[1],new_val)
                    if(new_tup not in visited):
                        queue.append(new_tup)
                
            if(node_tup[1]+1<n):
                new_val = node_tup[-1] + nums[node_tup[1]+1] 
                if(new_val%k==0):
                    return True
                else:
                    new_tup = (node_tup[0],node_tup[1]+1,new_val)
                    if(new_tup not in visited):
                        queue.append(new_tup)
        return False
    def checkSubarraySumOptimal(self, nums, k):
        myDict={0:-1} #For edge cases where the first index is included in the solution ex: [2,4] k=3
        total=0
        
        # Intuition here is that if we've already seen this remainder and that remainder is two indices away
        # if we discarded that number we'd have one that was a multiple of k. Simply brilliant
        for idx,n in enumerate(nums):
            total+=n
            
            if total%k not in myDict:
                myDict[total%k]=idx 
            
            elif idx - myDict[total%k]>=2:
                return True
        return False


if __name__ == "__main__":
    nums = [23,2,6,4,7]
    k = 6
    print(Solution().checkSubarraySum(nums,k))
    nums = [23,2,6,4,7]
    k = 13
    print(Solution().checkSubarraySum(nums,k))