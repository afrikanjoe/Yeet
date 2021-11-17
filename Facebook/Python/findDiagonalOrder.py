"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Exanoke: 
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
"""

class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        output = []
        right_moving = 2 
        queue = [(0,0)]
        while queue: 
            index = queue.pop()
            output.append(mat[index[0]][index[1]])
            if(right_moving%2==0):
                new_index = (index[0]-1,index[1]+1)
                if(new_index[0]>=0 and new_index[1]<n):
                    queue.append(new_index)
                else:
                    right_index = (index[0],index[1]+1)
                    bottom_index = (index[0]+1,index[1])
                    if(right_index[1]<n):
                        queue.append(right_index)
                    elif(bottom_index[0]<m):
                        queue.append(bottom_index)
                    right_moving+=1
            else:
                new_index = (index[0]+1,index[1]-1)
                if(new_index[1]>=0 and new_index[0]<m):
                    queue.append(new_index)
                else:
                    right_index = (index[0],index[1]+1)
                    bottom_index = (index[0]+1,index[1])
                    if(bottom_index[0]<m):
                        queue.append(bottom_index)
                    elif(right_index[1]<n):
                        queue.append(right_index)
                    right_moving+=1
        return output


if __name__ == "__main__":
    inp = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(Solution().findDiagonalOrder(inp))