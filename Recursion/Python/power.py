class Solution:
    @staticmethod
    def pow(x,n):
        if(n==0):
            return 1
        else:
            return x * pow(x,n-1)

if __name__ == "__main__":
    print(Solution.pow(4,3))