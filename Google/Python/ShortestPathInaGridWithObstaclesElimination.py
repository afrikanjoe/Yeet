"""

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
"""

class Solution:
    def shortestPath(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        goal = (m-1, n-1)
        paths = [] 
        shortestPath = -1
        # we will do dfs or bfs
        queue = [[(0,0)]]
        while len(queue)>0:
            path = queue.pop(0)
            node = path[-1]
            path_right = path[:]
            path_left = path[:]
            path_down = path[:]
            if(node) == goal:
                paths.append(path)
            else:
                nx,ny = node[0], node[1]
                if(nx+1 < m):
                    if (nx+1,ny) not in path_down:
                        path_down.append((nx+1,ny))
                        queue.append(path_down)
                if(ny+1 < n):
                    if((nx,ny+1) not in path_right):
                        path_right.append((nx,ny+1))
                        queue.append(path_right)
                if(ny>0):
                    if((nx,ny-1)) not in path_left:
                        path_left.append((nx,ny-1))
                        queue.append(path_left)
        
        # Iterate through the paths and eliminate those with more than 1 k
        for path in paths: 
            k_count = 0
            path_len = 0 
            skip_path = False
            for tup in path: 
                item = grid[tup[0]][tup[1]]
                if(item>0):
                    k_count+=1
                if(k_count>k):
                    skip_path = True
                    break 
                path_len+=1
            if(not skip_path):
                if(shortestPath<0):
                    shortestPath = path_len-1
                else:
                    shortestPath = min(shortestPath,path_len-1)
        return shortestPath



if __name__ == "__main__":
    grid = [[0,1,1],[1,1,1],[1,0,0]] 
    k = 1
    print(Solution().shortestPath(grid,k))
    grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
    k = 1
    print(Solution().shortestPath(grid,k))