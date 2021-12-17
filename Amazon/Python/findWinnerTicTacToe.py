class Solution:
    
    def __init__(self):
        self.board  = []
        self.n = 3 
        self.one_win = set([1])
        self.two_win = set([2])
        for i in range(self.n):
            self.board.append([0]*self.n)
    def tictactoe(self, moves):
        
        count=0
        for i in moves:
            self.board[i[0]][i[1]] = count%2+1
            if(self.validate_board()==1):
                return "A"
            elif(self.validate_board()==2):
                return "B"
            count+=1
            
        if(count==9):
            return "Draw"
        else:
            return "Pending"
        
        
        
    
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

if __name__ == "__main__":
    moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    print(Solution().tictactoe(moves))
    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    print(Solution().tictactoe(moves))
    moves = [[0,0],[1,1]]
    print(Solution().tictactoe(moves))