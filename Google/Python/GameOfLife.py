"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.


"""







class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        
        new_board = []
        for i in range(m):
            ls = [0]*n
            new_board.append(ls)
            
        
    
        for i in range(m):
            for j in range(n):
                
                neighs = self.get_neighbors((i,j),m,n,board)
                if(board[i][j]==1):
                    
                    if(neighs.get(1,0)<2 or neighs.get(1,0)>3):
                        new_board[i][j]=0
                    else:
                        new_board[i][j]=1
                    
                    
                else:
                    if(neighs.get(1,0)==3):
                        new_board[i][j]=1
                    else:
                        new_board[i][j]=0
        for i in range(m):
            for j in range(n):
                        
                board[i][j] = new_board[i][j]
        
    def get_neighbors(self,point,m,n,board):
        x = point[0]
        y = point[1]
        neighs = {}
        neighs2 = []
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if(i>=0 and i<m and j>=0 and j<n and (i,j)!=(x,y)):
                    
                    val = board[i][j]
                    neighs2.append(val)
                    neighs[val] = neighs.get(val,0)+1
        return neighs


if __name__ == "__main__":

    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print(board)
    print(Solution().gameOfLife(board))
    print(board)