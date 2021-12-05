"""
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. 
What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. 
It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:
"""

# no way I do this with anything other than numpy 
import numpy as np 


class Solution:

    def __init__(self):
        self.bingo_nums = []
        self.bingo_boards = []
    def read_input(self,file,count):
        self.bingo_nums = np.asarray(file.readline().split(",")).astype(int)
        file.readline()
        
        line_count = 2
        
        while line_count<count:
            curr_count = 0 
            board_mask = np.zeros((5,5))
            curr_board = []
            while curr_count<5:
                line = file.readline().replace("\n"," ").split(" ")
                line = [int(i) for i in line if i]
                if(len(line)>0):
                    curr_line = np.asarray(line).astype(int)
                    curr_board.append(curr_line)
                line_count+=1
                curr_count+=1
            
            if(len(curr_board)==5):
                curr_board = np.asarray(curr_board).reshape((5,5))
                self.bingo_boards.append([curr_board,board_mask])
            file.readline()
            line_count+=1
        

        winners = []
        win_vals = []
        for number in self.bingo_nums:
            for i in range(len(self.bingo_boards)):
                tup = self.bingo_boards[i]
                ans, new_mask, val  = self.update_board(tup[0],tup[1],number)
                if(ans):
                    if(i not in winners):
                        winners.append(i)
                        win_vals.append(val)
                new_tup = [tup[0],new_mask]
                self.bingo_boards[i] = new_tup
        print(winners,win_vals)


    def update_board(self,board,mask,value):
        val = np.where(board==value)
        mask[val] = 1
        ans, row = self.validate_row(board,mask)
        if(ans):
            return True, mask, row*value 
            #print("Answer Found:",row * val)
        return False, mask, 0 
        
    def validate_row(self,board,mask):
        for i in range(5):
            if(mask[i,:].sum(axis=0)==5):
                return True, board[np.where(mask<1)].flatten().sum()
        for i in range(5):
            if(mask[:,i].sum(axis=0)==5):
                return True, board[np.where(mask<1)].flatten().sum()
        return False, 0 
        


if __name__ == "__main__":
    with open("inputs/Day4.txt") as f:
        count = len(f.read().split("\n"))
        print(count)
    with open("inputs/Day4.txt") as f:
        s = Solution().read_input(f,count)