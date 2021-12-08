"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        count = m*n
        direction = 0
        x = 0 
        y = -1 
        additives = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
        visited = []
        while count>=0:
            adds =  additives[direction % 4]
            x_new = x + adds[0]
            y_new = y + adds[1]
            if(x_new>=0 and x_new<m and y_new>=0 and y_new<n):
                val = matrix[x_new][y_new]
                if((val,x_new,y_new) not in visited):
                    visited.append((val,x_new,y_new))
                    x = x_new
                    y = y_new
                else:
                    direction+=1
            else:
                direction+=1
            if(len(visited)==count):
                break
        
        ans = [i[0] for i in visited]
        return ans


if __name__ == "__main__":
    vals = [[1,2,3],[4,5,6],[7,8,9],[7,8,9]]
    print(Solution().spiralOrder(vals))