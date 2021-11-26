"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

class Solution:
    def exist(self, board, word):
        
        m = len(board)
        n = len(board[0])
        queue = []
        visited = []
        
        # add the starting positions to the queue
        for i in range(m):
            for j in range(n):
                if(board[i][j] == word[0]):
                    word_tup = (word[1:],i,j,[(i,j)])
                    queue.append(word_tup)
        
        while queue:
            remaining_word,i,j,tuple_list = queue.pop()
            if(not remaining_word):
                return True
            else:
                if(i-1>=0):
                    if(board[i-1][j]==remaining_word[0] and (i-1,j) not in tuple_list):
                        word_tup = (remaining_word[1:],i-1,j,tuple_list+[(i-1,j)])
                        queue.append(word_tup)
                    
                    
                    
                if(j-1>=0):
                    if(board[i][j-1]==remaining_word[0] and (i,j-1) not in tuple_list):
                        word_tup = (remaining_word[1:],i,j-1,tuple_list+[(i,j-1)])
                        queue.append(word_tup)
                if(i+1<m):
                     if(board[i+1][j]==remaining_word[0] and (i+1,j) not in tuple_list):
                        word_tup = (remaining_word[1:],i+1,j,tuple_list+[(i+1,j)])
                        queue.append(word_tup)
                if(j+1<n):
                    if(board[i][j+1]==remaining_word[0] and (i,j+1) not in tuple_list):
                        word_tup = (remaining_word[1:],i,j+1,tuple_list+[(i,j+1)])
                        queue.append(word_tup)
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(Solution().exist(board,word))