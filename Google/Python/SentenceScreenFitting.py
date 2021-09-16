"""
Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

"""

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        count = 0 
        grid = []
        for i in range(rows):
            grid.append(['']*cols)
        i = 0 
        j = 0 
        word_counter = 0
        while(i<rows):
            word = sentence[word_counter%len(sentence)] 
            if(len(word)<=len(grid[i][j:])):
                for k in range(len(word)):
                    grid[i][j] = word[k]
                    j+=1
                word_counter+=1
                if(j<cols):
                    grid[i][j] = '-'
                    j+=1
            elif(j<=cols):
                for j in range(j,cols):
                    grid[i][j] = '-'
                i+=1
                j=0
            #print(grid)
        return word_counter // len(sentence)

if __name__ == "__main__":
    inp = ["hello","world"]
    rows, cols = 2 , 8
    print(Solution().wordsTyping(inp,rows,cols))
    inp = ["a", "bcd", "e"]
    rows = 3
    cols = 6
    print(Solution().wordsTyping(inp,rows,cols))
    inp = ["i","had","apple","pie"]
    rows = 4 
    cols = 5
    print(Solution().wordsTyping(inp,rows,cols))