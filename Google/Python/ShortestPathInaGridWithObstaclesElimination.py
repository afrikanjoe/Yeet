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


        """
        One way to improve this solution is to only explore paths that have less than the required number of obstacles. 
        This prevents you from having to explore paths
        """

        def shortestPath(self, grid: List[List[int]], k: int) -> int:
            M,N=len(grid),len(grid[0])

            steps=0
            q,seen=[(0,0,0)],set()
            while q:
                for _ in range(len(q)):
                    r,c,used=q.pop(0)
                    if (r,c)==(M-1,N-1):
                        return steps
                    for x,y in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
                        if 0<=x<M and 0<=y<N and (x,y,used) not in seen:
                            if grid[x][y]==0:
                                q.append((x,y,used))
                                seen.add((x,y,used))
                            elif grid[x][y]==1 and used<k:
                                seen.add((x,y,used))
                                q.append((x,y,used+1))
                steps+=1
            return -1



if __name__ == "__main__":
    grid = [[0,1,1],[1,1,1],[1,0,0]] 
    k = 1
    print(Solution().shortestPath(grid,k))
    grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
    k = 1
    print(Solution().shortestPath(grid,k))