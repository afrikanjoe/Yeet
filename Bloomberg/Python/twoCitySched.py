"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.


"""

import heapq
class Solution:
    def twoCitySchedCost(self, costs):
        
        a_heap = []
        for cost in costs:
            heapq.heappush(a_heap, (cost[1]-cost[0],cost))
        
        
        counts = {"a":0,"b":0}
        k = int(len(a_heap)/2)
        ans = 0 
        for i in range(k):
            val = heapq.heappop(a_heap)
            ans+= val[1][1]
            
        for i in range(k):
            val = heapq.heappop(a_heap)
            ans+= val[1][0]
            
        return ans

if __name__ == "__main__":
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    print(Solution().twoCitySchedCost(costs))
        