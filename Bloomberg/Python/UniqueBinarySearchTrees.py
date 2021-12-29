"""
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.
"""

class Solution:
    
    # The answer to this question is a niche mathematical deduction relation 
    # used to compute something called a Catalan number, this some bs
    def numTrees(self, n):
        C = 1
        for i in range(0,n):
            
            C = (2*(2*i+1) / (i+2))*C
            
        return int(C)

if __name__ == "__main__":
    n = 19 
    print(Solution().numTrees(n))

