"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.


    x << y
        Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
    x >> y
        Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
    x & y
        Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
    x | y
        Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
    ~ x
        Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
    x ^ y
        Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.


"""

class Solution:
    def singleNumberBruteForce(self, nums):
        count = {}
        for i in nums:
            count[i]= count.get(i,0) + 1
        for pair in count.items():
            if(pair[1]==1):
                return pair[0]

    """ XOR is frequently used to check the parity of bits and that's why it works in this context
    Essentially we are treating everything as a bit and so two XOR with the same number will negate each other
    leaving the missing number for example in the example below it goes
    100 ->101 ->111 -> 110 -> 100 which is our result
    
    
    
    
    """
    def singleNumber(self, nums):
        ans=0
        for i in nums:
            print(i)
            ans^=i
            print("ans:",ans)
        return ans


if __name__=="__main__":

    inp = [4,1,2,1,2]
    sol = Solution()
    print("Brute Force:",sol.singleNumberBruteForce(inp))
    print(sol.singleNumber(inp))