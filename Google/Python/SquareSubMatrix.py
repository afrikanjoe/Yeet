"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

class Solution:
    def countSquares(self, matrix):
        start = 1
        m, n = len(matrix),len(matrix[0])
        end = min(m,n)
        one_count = 0

        for i in range(start,end+1):
            for j in range(0,m-i+1):
                list1 = matrix[j:j+i]
                if(len(list1)!=i):
                    continue
                for k in range(0,n-i+1):
                    temp_ls = []
                    count = True
                    for ls in list1:
                        if(0 in ls[k:k+i]):
                            count = False
                        temp_ls.append(ls[k:k+i])
                    if(count):
                        one_count+=1
        return one_count
        

if __name__ == "__main__":
    matrix = [
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ]

    print(Solution().countSquares(matrix))

    matrix =[
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
    ]

    print(Solution().countSquares(matrix))