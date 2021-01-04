import math

"""  
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    @staticmethod
    def rotatecopy(matrix):
        rot = math.radians(-90)
        add = len(matrix)
        returnarr = [[0]*3 for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                x = round((i+1)*math.cos(rot) - (j+1)*math.sin(rot))
                y = round((i+1)*math.sin(rot) + (j+1)*math.cos(rot))

                returnarr[x-1][y+add] = matrix[i][j]
        return returnarr

    # had to do this on paper
    # tranpose and then reverse
    @staticmethod
    def rotate(matrix):
        addressed = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if((i,j) in addressed):
                    continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i]= temp 
                    addressed.append((i,j))
                    addressed.append((j,i))
        #reverse
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


if __name__=='__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution.rotatecopy(matrix))
    Solution.rotate(matrix)
    print(matrix)