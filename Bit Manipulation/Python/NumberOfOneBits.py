"""
n & n-1 will remove the right most 1 from n.
(n-1) flips right-most 1 and everything right of that
tip: you can use n & n-1 == 0 to check whether a given number n is a power of 2 because 
all powers of 2 only have a single 1. i.e 
n = 32 = 100000
 &
n-1=31 = 011111
----------------
n&(n-1)= 000000

"""



class Solution:
    def hammingWeight(self,n):
        n = "{0:b}".format(n)
        count = 0
        for i in n:
            if (i=='1'):
                count+=1
        return count

    def hammingWeightMagic(self,n):
        count = 0 
        while (n!=0):
            n = n & (n -1)
            count+=1
        return count


if __name__=="__main__":
    inp = 5
    sol = Solution()
    print("Brute Force:",sol.hammingWeight(inp))
    print("Magic:",sol.hammingWeightMagic(inp))