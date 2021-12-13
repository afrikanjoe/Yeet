"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
"""

from collections import Counter 
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        c = Counter(arr)
        heap = []
        
        for key in c:
            
            
            heapq.heappush(heap,(c[key],key))        
        
        for i in range(k):
            
            if(len(heap)>0):
                
                count,val = heapq.heappop(heap)
                
                if(count-1>0):
                    
                    heapq.heappush(heap,(count-1,val)) 
        return len(heap)


if __name__ == "__main__":
    arr = [4,3,1,1,3,3,2]
    k = 3
    print(Solution().findLeastNumOfUniqueInts(arr,k))