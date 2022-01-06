
"""The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.
"""

class Solution:
    def bitwiseComplement(self, n):
        a= str(bin(n))[2:]
        new_a = []
        for i in a:
            if(i=="1"):
                new_a.append("0")
            else:
                new_a.append("1")
        new_a = "".join(new_a)
        return int(new_a,2)

if __name__ == "__main__":
    n = 9
    print(Solution().bitwiseComplement(n))