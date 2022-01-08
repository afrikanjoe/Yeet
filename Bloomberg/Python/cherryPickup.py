"""
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.


"""
class Solution:
    def cherryPickup(self, grid):
        maxa = -2**32
        if(not grid):
            return 0 
        queue1 = [  [ [[0,0,grid[0][0]]],[[0,len(grid[0])-1,grid[0][-1]]]] ]
        m = len(grid)
        n = len(grid[0])
        
        while queue1:
            
            paths = queue1.pop()
            rob1_path  = paths[0]
            rob2_path  = paths[1]
            
            # rob1
            
            added = False
            for i in range(-1,2):
                last_point= [rob1_path[-1][0]+1,rob1_path[-1][1]+i]
                for j in range(-1,2):
                    last_point2 = [rob2_path[-1][0]+1,rob2_path[-1][1]+j]
                    
                    if(last_point[0]<m and last_point[1]>=0 and last_point[1]<n  and last_point2[0]<m and last_point2[1]>=0 and last_point2[1]<n ):
                        added = True
                        if(last_point==last_point2):

                            new_path = rob1_path[:] + [last_point+[rob1_path[-1][2]+grid[last_point[0]][last_point[1]]]]
                            new_path1 = rob1_path[:] + [last_point+[rob1_path[-1][2]+0]]

                            new_path2 = rob2_path[:] + [last_point2+[rob2_path[-1][2]+grid[last_point2[0]][last_point2[1]]]]
                            new_path3 = rob2_path[:] + [last_point2+[rob2_path[-1][2]+0]]
                            
                            
                            p1 = [new_path,new_path3]
                            p2 = [new_path1,new_path2]
                            queue1.append(p1)
                            queue1.append(p2)
                        else:
                            
                            new_path = rob1_path[:] + [last_point+[rob1_path[-1][2]+grid[last_point[0]][last_point[1]]]]
                            new_path2 = rob2_path[:] + [last_point2+[rob2_path[-1][2]+grid[last_point2[0]][last_point2[1]]]]
                            queue1.append([new_path,new_path2])
            if(not added):
                maxa = max(maxa,paths[1][-1][2]+paths[0][-1][2])
        return maxa

from functools import lru_cache


class OptimalSolution:
    def cherryPickup(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        @lru_cache(None)
        def helper(row,col1,col2):
            if(col1<0 or col2<0 or col1>=n or col2>=n):
                return - 2**32
            
            result = 0 
            result+=grid[row][col1]
            if(col1!=col2):
                result+=grid[row][col2]
                
            if(row<m-1):
                curr_row = row+1
                sub_cases = [helper(curr_row,new_col1,new_col2) 
                             for new_col1 in [col1,col1+1,col1-1]
                             for new_col2 in [col2,col2+1,col2-1]
                            ]
                result += max(sub_cases)
                
            return result
        
        return helper(0,0,n-1)

if __name__ == "__main__":
    nums = [[8,8,10,9,1,7],[8,8,1,8,4,7],[8,6,10,3,7,7],[3,0,9,3,2,7],[6,8,9,4,2,5],[1,1,5,8,8,1],[5,6,5,2,9,9],[4,4,6,2,5,4],[4,4,5,3,1,6],[9,2,2,1,9,3]]
    print(OptimalSolution().cherryPickup(nums))