"""

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] 
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

"""

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        
        adj_list = {}
        paths = []
        for i in range(len(edges)):
            edge = edges[i]
            prob = succProb[i]
            val = adj_list.get(edge[0],[])
            val.append((edge[1],prob))
            
            val2 = adj_list.get(edge[1],[])
            val2.append((edge[0],prob))
            
            adj_list[edge[0]] = val
            adj_list[edge[1]] = val2
        
        queue =  [[(start,1)]]
        while queue:
            
            curr_path = queue.pop(0)
            last_node = curr_path[-1]
            if(last_node[0]==end):
                paths.append(curr_path)
            else:
                
                neighbors = adj_list.get(last_node[0],[])
                for neighbor in neighbors:
                    if(neighbor not in curr_path):
                        new_list = curr_path[:] + [neighbor]
                        queue.append(new_list)
        
        max_prob = 0
        for path in paths: 
            
            mult = 1
            for i in path: 
                mult*=i[1]
            max_prob = max(max_prob,mult)
                        
        
        
        
        return max_prob