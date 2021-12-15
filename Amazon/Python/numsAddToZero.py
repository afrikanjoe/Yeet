"""

Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

class Solution:

    def sumZero(self, n):
        ans = list(range(1,n)) + [-self.natural_sum(n-1)]
        return ans
        
        
    def natural_sum(self,n):
        return int(n*(n+1)/2)

if __name__ == "__main__":
    print(Solution().sumZero(100))