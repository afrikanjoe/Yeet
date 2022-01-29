"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

"""
class Solution:
    def convert(self, s, numRows):
        if(numRows==1):
            return s
        matrix = []
        for i in range(numRows):
            matrix.append([""]*len(s))
        
        
        direction = [[1,0],[-1,1]]
        count = 0 
        ind = (-1,0)
        
        letters = list(s)
        while letters:
            new_index = (ind[0]+direction[count%2][0],ind[1]+direction[count%2][1])
            if(new_index[0]<numRows and new_index[0]>=0):
                letter = letters.pop(0)
                matrix[new_index[0]][new_index[1]] = letter
                ind = new_index
            else:
                count+=1
        return_str = ""
        for row in matrix:
            return_str = return_str + "".join(row)
        return return_str


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s,numRows))