"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""

class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                try: 
                    board[i][j] = int(board[i][j])
                except:
                    board[i][j] = 0
                    
        return self.check3b3(board) and self.check_rows(board) and self.check_columns(board)
    def check_rows(self,board):
        for row in board:
            curr_list = []
            for val in row:
                if(val in curr_list):
                    return False
                elif(val>0):
                    curr_list.append(val)
        return True
        
    def check_columns(self,board):
        for col in range(9):
            curr_list = []
            for row in range(9):
                val = board[row][col]
                if(val in curr_list):
                    return False
                elif(val>0):
                    curr_list.append(val)  
        return True
    
    def check3b3(self,board):
        for i in range(0,9,3):
            for j in range(0,9,3):
                curr_list = []
                for k in range(i,i+3):
                    for h in range(j,j+3):
                        val = board[k][h]
                        if(val in curr_list):
                            return False
                        elif(val>0):
                            curr_list.append(val)
        return True
                
if __name__ == "__main__":
    board = [["7",".",".",".","4",".",".",".","."],
    [".",".",".","8","6","5",".",".","."],
    [".","1",".","2",".",".",".",".","."],
    [".",".",".",".",".","9",".",".","."],
    [".",".",".",".","5",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]

    print(Solution().isValidSudoku(board))