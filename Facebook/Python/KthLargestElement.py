"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        
        count = 0
        val = 0 
        for i in range(k):
            val = heapq.heappop(heap)
        return -val

if __name__ == "__main__":
    nums =[3,2,3,1,2,4,5,5,6]
    k = 4
    print(Solution().findKthLargest(nums,k))