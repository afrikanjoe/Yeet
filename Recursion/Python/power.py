class Solution:
    @staticmethod
    def power(x,n):
        if(n<0):
            x = (1.0/x)
            n= abs(n)
        if(n==0):
            return 1
        else:
            return x * Solution.power(x,n-1)

if __name__ == "__main__":
    print(Solution.power(4,-3))
    print(Solution.power(4,3))
    print(Solution.power(2,3))