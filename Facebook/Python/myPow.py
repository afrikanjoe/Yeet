class Solution:
    def myPowBF(self, x, n):
        
        start = x
        mult = x
        if(n<0):
            n = n-2
        elif(n==0):
            return 1
        for i in range(abs(n)-1):
            if(n<0):
                start = start / mult
            else:
                start = start* mult
        return start
        
    
    # insight from mathematical rules 
    # this is pretty elegant
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        return x * self.myPow(x, n - 1) if n % 2 else self.myPow(x * x, n // 2)
        



if __name__ == "__main__":
    x = 0.00001
    n = 2147483647
    print(Solution().myPow(x,n))
