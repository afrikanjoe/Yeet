"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.The area of an island is the 
number of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island, return 0.

"""


class Solution:
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        explored = []
        max_area = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] and (i,j) not in explored):
                    max_area = self.explore(grid,i,j,explored,max_area)
        return max_area
    
    def  explore(self, grid,i,j, explored,max_area):
        m = len(grid)
        n = len(grid[0])
        island = [(i,j)]
        queue = [(i,j)]
        while queue: 
            node = queue.pop(0)
            i,j = node[0], node[1]
            explored.append(node)
            if(i-1>=0):
                if(grid[i-1][j] and (i-1,j) not in island):
                    island.append((i-1,j))
                    queue.append((i-1,j))
                    explored.append((i-1,j))
            if(i+1<m):
                if(grid[i+1][j] and (i+1,j) not in island):
                    island.append((i+1,j))
                    queue.append((i+1,j))
                    explored.append((i+1,j))
            if(j-1>=0):
                if(grid[i][j-1] and (i,j-1) not in island):
                    island.append((i,j-1))
                    queue.append((i,j-1))
                    explored.append((i,j-1))
            if(j+1<n):
                if(grid[i][j+1] and (i,j+1) not in island):
                    island.append((i,j+1))
                    queue.append((i,j+1))
                    explored.append((i,j+1))

        return max(len(island),max_area)

if __name__ == "__main__":

    ### Expected Solution = 6
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(Solution().maxAreaOfIsland(grid))

    ### Expected Solution = 0 
    grid = [[0,0,0,0,0,0,0,0]]
    print(Solution().maxAreaOfIsland(grid))

    ### Expected Solution = 3
    grid = [[0,1],[1,1]]
    print(Solution().maxAreaOfIsland(grid))