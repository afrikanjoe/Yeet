"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_indices = []
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    zero_indices.append((i,j))
                    
        
        
        for tup in zero_indices:
            self.set_colrow_zero(tup,matrix)
                    
    
    def set_colrow_zero(self,zero_index,matrix):
        x = zero_index[0]
        y = zero_index[1]
        # above
        for i in range(x,-1,-1):
            matrix[i][y] = 0 
        
        # below
        for i in range(x,len(matrix)):
            matrix[i][y] = 0 
            
        # left
        for i in range(y,-1,-1):
            matrix[x][i] = 0 
        
        # right
        for i in range(y,len(matrix[0])):
            matrix[x][i] = 0 


if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(matrix)
    Solution().setZeroes(matrix)
    print(matrix)