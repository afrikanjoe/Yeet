"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
"""

class Solution:
    def getMaximumGold(self, grid):
        
        
        m = len(grid)
        n = len(grid[0])
        res = []
        queue = []
        for i in range(m):
            for j in range(n):
                grid[i][j]= int(grid[i][j])
                if(grid[i][j]>0):
                    queue.append([(i,j)])
                    
        while queue:
            val_list = queue.pop(0)
            grid_point = val_list[-1]
            added = False
            if(grid_point[0]-1>=0):
                if(grid[grid_point[0]-1][grid_point[1]]>0 and (grid_point[0]-1,grid_point[1]) not in val_list):
                    added = True
                    ls = val_list[:]
                    ls.append((grid_point[0]-1,grid_point[1]))
                    queue.append(ls)
            if(grid_point[0]+1<m):
                if(grid[grid_point[0]+1][grid_point[1]]>0 and (grid_point[0]+1,grid_point[1]) not in val_list):
                    added = True
                    ls = val_list[:]
                    ls.append((grid_point[0]+1,grid_point[1]))
                    queue.append(ls)
            if(grid_point[1]-1>=0):
                if(grid[grid_point[0]][grid_point[1]-1]>0 and (grid_point[0],grid_point[1]-1) not in val_list):
                    added = True
                    ls = val_list[:]
                    ls.append((grid_point[0],grid_point[1]-1))
                    queue.append(ls)
            if(grid_point[1]+1<n):
                if(grid[grid_point[0]][grid_point[1]+1]>0 and (grid_point[0],grid_point[1]+1) not in val_list):
                    added = True
                    ls = val_list[:]
                    ls.append((grid_point[0],grid_point[1]+1))
                    queue.append(ls)
            if(not added):
                res.append(val_list)
        
        max_val = 0 
        for i in res:
            curr_sum = 0
            for tup in i:
                x = tup[0]
                y = tup[1]
                curr_sum+= grid[x][y]
                max_val = max(max_val,curr_sum)

            
            
        return max_val


if __name__ == "__main__":
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(Solution().getMaximumGold(grid))
