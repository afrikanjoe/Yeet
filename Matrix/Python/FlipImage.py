
"""Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0]."""

class Solution:
    @staticmethod
    def flipAndInvertImage(A):
        returnarr = []
        for i in range(len(A)):
            temp = []
            for j in A[i][::-1]:
                temp.append(j^1)
            returnarr.append(temp)
        return returnarr


if __name__=="__main__":
    image = [[1,1,0],[1,0,1],[0,0,0]]
    print(Solution.flipAndInvertImage(image))