"""
You have a 2-D grid of size m x n representing a box, and you have n balls. 
The box is open on the top and bottom sides.Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck 
if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.
"""

class Solution:
    # My attempt
    def findBallPat(self, grid):
        m = len(grid)
        n = len(grid[0])
        print(m,n)
        ans = []
        for i in range(n):
            j=0
            k = i
            early_terminate = False
            prev = None
            while j < m and k<n:
                entry = grid[j][k]
                # check for being stuck next to the wall 
                if(k==0 and entry<0):
                    ans.append(-1)
                    early_terminate = True
                    break
                elif(k==n-1 and entry>0):
                    ans.append(-1)
                    early_terminate = True
                    break
                elif(grid[j][k:k+2]==[1,-1]):
                        ans.append(-1)
                        early_terminate = True
                        break
                elif(grid[j][k:k+2]==[-1,1]):
                    if(prev==-1):
                        ans.append(-1)
                        early_terminate = True
                        break
                prev = entry
                if(entry>0):
                    k+=1
                else:
                    k-=1
                j+=1
            if not (early_terminate):
                ans.append(k)
        return ans 
    
    def findBall(self,grid):
        n,m = len(grid[0]),len(grid)
        # create list with indices
        ball = [n for n in range(n)]
        for row in range(m):
            for index,col in enumerate(ball):
                if (col != -1):
                    # get the column index and add the value stored in the grid
                    adjacent_cell_index = col + grid[row][col]
                    print(adjacent_cell_index)
                    # Hit the walls of form a 'V'
                    # if we are moving left we need to check to the left and if we are moving to the right 
                    # then check the right                 
                    if (0 < adjacent_cell_index >= n or grid[row][col] != grid[row][adjacent_cell_index]):
                        ball[index] = -1
                    else:
                        ball[index] += grid[row][col]
        return ball



if __name__=="__main__":

    # Expected Solution: [1,-1,-1,-1,-1]
    inputGrid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    print(Solution().findBall(inputGrid))

    # Expected Solution: [0,1,2,3,4,-1]
    inputGrid2 = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    print(Solution().findBall(inputGrid2))

    inputGrid3 = [[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]
    print(Solution().findBall(inputGrid3))