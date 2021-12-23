
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        queue = [([(0,0)],grid[0][0])]
        min_sum = 2**32
        
        while queue:
            
            curr_list, curr_sum = queue.pop()
            x,y = curr_list[-1]
            
            if(x==m-1 and y==n-1):  
                min_sum = min(min_sum,curr_sum)
            else:
                if(x+1<m):

                    new_list = curr_list[:] + [(x+1,y)]
                    new_sum = curr_sum + grid[x+1][y]
                    
                    queue.append((new_list,new_sum))
                    
                if(y+1<n):

                    new_list = curr_list[:] + [(x,y+1)]
                    new_sum = curr_sum + grid[x][y+1]
                    queue.append((new_list,new_sum))
        return min_sum

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))

            