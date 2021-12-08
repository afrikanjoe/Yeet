"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n^2).
"""

import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                heapq.heappush(heap,matrix[i][j])
                
        for i in range(1,k):
            
            heapq.heappop(heap)
        return heap[0]
        

if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(Solution().kthSmallest(matrix,k))
