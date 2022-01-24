class Solution:
    @staticmethod
    def fairIndices(A,B):
        count = 0 
        for i in range(1,len(A)):
            sum_a_left  = sum(A[0:i])
            sum_a_right = sum(A[i:])
            sum_b_left = sum(B[0:i])
            sum_b_right = sum(B[i:])
            if(sum_a_left==sum_a_right and sum_a_left==sum_b_left and sum_a_left==sum_b_right):
                #print("index:",i)
                count+=1
        return count 

if __name__ == "__main__":
    A = [0,4,-1,0,3]
    B = [0,-2,5,0,3]
    print(Solution.fairIndices(A,B))

    A = [2,-2,-3,3]
    B = [0,0,4,-4]
    print(Solution.fairIndices(A,B))

    A = [4,-1,0,3]
    B = [-2,6,0,4]
    print(Solution.fairIndices(A,B))

    A = [3,2,6]
    B = [4,1,6]
    print(Solution.fairIndices(A,B))

    A = [1,4,2-2,5]
    B = [7,-2,-2,2,5]
    print(Solution.fairIndices(A,B))

