"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        index = 0 
        
        for i in range(m-1):
            for j in range(n-1):
                if(i+1<m and j+1<n):
                    if(matrix[i][j]!=matrix[i+1][j+1]):
                        return False
        return True
        

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(Solution().isToeplitzMatrix(matrix))
    matrix = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
    print(Solution().isToeplitzMatrix(matrix))