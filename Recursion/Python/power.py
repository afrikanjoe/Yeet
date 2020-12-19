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

    @staticmethod
    def power1(x, n):
        if(n==0):
            return 1 
        if(n>0):
            if(n%2==0):
                return Solution.power1(x*x,n/2)
            else:
                return x * Solution.power1(x*x,(n - 1) / 2)
        else:
            return 1.0 / Solution.power1(x,-n)

if __name__ == "__main__":
    print(Solution.power(4,-3))
    print(Solution.power(4,3))
    print(Solution.power(2,3))