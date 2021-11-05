"""
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.


Input: mat = [[0,0],[0,1]]
Output: 1
"""


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        
        dimensions_list = binaryMatrix.dimensions()
        m = dimensions_list[0]
        n = dimensions_list[1]
        column = n+1
        for row in range(m):
            start = 0
            end = n - 1
            while start <= end:
                mid = (start+end)>>1
                val = binaryMatrix.get(row,mid)
                
                if(val==1):
                    column = min(column,mid)
                    end = mid-1
                else:
                    start = mid+1
                    
                if(column==0):
                    return column 
        if(column<n):
            return column
        return  -1 

if __name__ == "__main__":
    inp = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    print(Solution().leftMostColumnWithOne(inp))