"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""
from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost = tuple(cost)
        @lru_cache(None)
        def helper(index,costs):
            if(index>=n):
                return costs
            elif(index==n-1):
                return costs+cost[n-1]
            else:
                return costs+min(helper(index+1,cost[index]),helper(index+2,cost[index]))
        return min(helper(0,0),helper(1,0))

if __name__ == "__main__":

    costs = [1,100,1,1,1,100,1,1,100,1,1,100,1,1,1,100,1,1,100,1]
    print(Solution().minCostClimbingStairs(costs))