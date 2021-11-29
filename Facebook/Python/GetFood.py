"""
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

"""

class Solution:
    def getFood(self, grid):
        m = len(grid)
        n = len(grid[0])
        queue = []
        results  = []
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=="*"):
                    queue.append([(i,j,"*")])
                    break
        visited = []
        while queue: 
            
            c_list = queue.pop(0)
            c_i,c_j,c_v = c_list[-1]
            visited.append((c_i,c_j))
            if(c_v=="#"):
                results.append(c_list)
            else:
                if((c_i+1)<m and ((c_i+1,c_j,'O') not in c_list)):
                    if((grid[(c_i+1)][c_j] == 'O' or grid[(c_i+1)][c_j] == '#')):
                        new_list = c_list[:]
                        new_list.append((c_i+1,c_j,grid[(c_i+1)][c_j]))
                        queue.append(new_list)
                if((c_j+1)<n and (c_i,c_j+1,'O') not in c_list):
                    if((grid[(c_i)][c_j+1] == 'O' or grid[(c_i)][c_j+1] == '#')):
                        new_list = c_list[:]
                        new_list.append((c_i,c_j+1,grid[(c_i)][c_j+1]))
                        queue.append(new_list)
                if((c_i-1)>=0  and (c_i-1,c_j,'O') not in c_list):
                    if((grid[(c_i-1)][c_j] == 'O' or grid[(c_i-1)][c_j] == '#')):
                        new_list = c_list[:]
                        new_list.append((c_i-1,c_j,grid[(c_i-1)][c_j]))
                        queue.append(new_list)
                
                if((c_j-1)>=0  and (c_i,c_j-1,'O') not in c_list):
                    if((grid[(c_i)][c_j-1] == 'O' or grid[(c_i)][c_j-1] == '#')):
                        new_list = c_list[:]
                        new_list.append((c_i,c_j-1,grid[c_i][c_j-1]))
                        queue.append(new_list)
        if(not results):
            return -1 
        else:
            min_val = 2**32
            for i in results:
                min_val = min(len(i)-1,min_val)
            return min_val

if __name__ == "__main__":
    grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],
    ["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
    print(Solution().getFood(grid))