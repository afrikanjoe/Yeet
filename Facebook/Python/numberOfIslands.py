"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.

"""

class Solution:
    def numIslands(self, grid):
        queue = []
        res = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                grid[i][j]= int(grid[i][j])
                if(grid[i][j]==1):
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
                    
                    
            val_list =  sorted(val_list)      
            if(not added and val_list not in res):
                add = True
                for i in range(len(res)):
                    if(i>=len(res)):
                        break
                    for val in val_list:
                        item = res[i]
                        if(val in item):
                            if(len(val_list)>len(item)):
                                if(val_list not in res):
                                    res[i] = val_list
                                else:
                                    res.pop(i)
                            add = False
                            break
                
                if(add):
                    res.append(sorted(val_list))
        return len(res)


if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(Solution().numIslands(grid))

    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(Solution().numIslands(grid))



