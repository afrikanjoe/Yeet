"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. 
The move is guaranteed to be a valid move.
"""

class TicTacToe:

    def __init__(self, n):
        
        self.board = []
        self.one_win = set([1])
        self.two_win = set([2])
        self.n = n
        for i in range(n):
            self.board.append([0]*n)
        
    def validate_board(self):
        # check rows 
        for row in self.board:
            if(set(row)==self.one_win):
                return 1
            elif(set(row)==self.two_win):
                return 2
        
        # check columns
        for i in range(self.n):
            col = [self.board[j][i]  for j in range(self.n)]
            if(set(col)==self.one_win):
                return 1
            elif(set(col)==self.two_win):
                return 2
            
        # chech diagonals 
        diaga = []
        diagb = []
        
        diag_bx = self.n-1
        diag_by = 0
        for i in range(self.n):
            diaga.append(self.board[i][i])
            diagb.append(self.board[diag_bx][diag_by])
            diag_bx-=1
            diag_by+=1
            
        if(set(diaga)==self.one_win or set(diagb)==self.one_win):
                return 1
        elif(set(diaga)==self.two_win or set(diagb)==self.two_win):
            return 2
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self.validate_board()
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)