"""

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.
"""
from functools import lru_cache
class Solution:
    def minCost(self, costs):
        
        n = len(costs)
        
        queue = [([i],costs[0][i]) for i in range(3)]
        min_cost = 2**32
        while queue:
            
            entry = queue.pop()
            if(len(entry[0])==n):
                min_cost = min(entry[1],min_cost)
            else:
                
                last_house = entry[0][-1]
                
                for i in range(3):
                    if(i==last_house):
                        continue
                    new_entry_list = entry[0][:] + [i]
                    new_cost = entry[1] + costs[len(entry[0])][i]
                    queue.append((new_entry_list,new_cost))
                    
        return min_cost

class OptimalSolution:
    def minCost(self, costs):
        
        @lru_cache(maxsize=None)
        def paint(n,color):
            total_costs = costs[n][color]
            if(n==len(costs)-1):
                pass
            else:
                if(color==0):
                    total_costs+=min(paint(n+1,1),paint(n+1,2))
                elif(color==1):
                    total_costs+=min(paint(n+1,0),paint(n+1,2))
                else:
                    total_costs+=min(paint(n+1,0),paint(n+1,1))
            return total_costs
        
        return min(paint(0,0),paint(0,1),paint(0,2))
                    

if __name__ == "__main__":
    house_costs = [[7,8,12],[18,16,1],[14,7,7],[16,2,20],[9,13,18],[14,18,17],[7,10,6],[8,4,11],[20,5,2],[9,8,4],[13,1,6],[2,3,10],[7,4,16],[7,19,17],[10,6,8],[14,6,13],[15,7,6]]
    print(OptimalSolution().minCost(house_costs))
                
        
        