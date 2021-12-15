import heapq

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""

class Solution:
    def longestConsecutive(self, nums):
        
        if(not nums):
            return 0
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            
        consec = 0 
        count = 0
        prev = heap[0]-1
        while heap:
            val = heapq.heappop(heap)
            if(val-prev==1):
                count+=1
            elif(val-prev==0):
                continue
            else:
                consec = max(count,consec)
                count=1
            prev = val
        
        consec = max(count,consec)
        return consec

if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(Solution().longestConsecutive(nums))