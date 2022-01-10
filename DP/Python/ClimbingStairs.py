"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


from functools import lru_cache

class Solution:
    def climbStairs(self, n):
        @lru_cache(None)
        def helper(n):
            if(n<0):
                return 0
            elif(n==1 or n==0):
                return 1 
            else:
                return helper(n-1) + helper(n-2)
        return helper(n)

if __name__ == "__main__":
    n = 30
    print(Solution().climbStairs(n))