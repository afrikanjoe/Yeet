from functools import lru_cache
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Recursion with memoization is how you solve this problem and from functools import lru_cache is one way of doing this
The first attempt I did also works but I need to store my solutions and keep track of them
"""
class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n):
        if(n<0):
            return 0
        elif(n==1 or n==0):
            return 1
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
        #print(visited)
        return count
    def climbStairsAttempt1(self, n):
        queue = [[]]
        count = 0 
        visited = []
        while queue:
            val = queue.pop()
            if(sum(val)==n):
                visited.append(val)
                count+=1
            for i in range(1,3):
                new_list = val[:] + [i]
                if(sum(new_list)<=n):
                    queue.append(new_list)
        return count
if __name__ == "__main__":
    n = 35
    print(Solution().climbStairs(n))
    
