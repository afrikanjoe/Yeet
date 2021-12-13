"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. 
The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road 
between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between 
intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to 
intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, 
return it modulo 109 + 7.


"""

from sortedcontainers import SortedDict

class Solution:
    def countPaths(self, n, roads):
        
        adj_list = {}
        value_dict = {}
        paths = []
        for road in roads:
            
            val1 = adj_list.get(road[0],[])
            val1.append((road[1],road[2]))
            
            adj_list[road[0]] = val1
            
            val2 = adj_list.get(road[1],[])
            val2.append((road[0],road[2]))
            
            adj_list[road[1]] = val2
            
        queue = [[(0,0)]]
        
        while queue: 
            curr_path = queue.pop()
            last_node = curr_path[-1]
            if last_node[0]==(n-1):
                paths.append(curr_path)
            else:
                ns = adj_list.get(last_node[0],[])
                for i in ns:
                    if(i not in curr_path):
                        new_list = curr_path[:]+ [i]
                        queue.append(new_list)
        for path in paths:
            
            time = 0 
            for node in path: 
                time+=node[1]
            value_dict[time] = value_dict.get(time,0)+1
        
        d = SortedDict(value_dict)
        last = d.items()[0][1]
        return last
                
                
            
            
            
            
            
        