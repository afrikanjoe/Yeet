"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.
"""

class Solution:
    def countComponents(self, n, edges):
        
        paths = []
        adj_list = {}
        in_degree = {}
        for i in range(n):
            adj_list[i] = []
            in_degree[i] = 0 
        
        for edge in edges:
            edge = sorted(edge)
            in_degree[edge[1]]+=1
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            
        
        
        ns = []
        for i in range(n):
            if(in_degree[i]==0):
                ns.append(i)
    
        for i in ns:
            path = self.bfs(i,adj_list)
            if(path not in paths):
                paths.append(path)
                
        return len(paths)
            
        
    
    def bfs(self,node,adj_list):
        queue = [node]
        visited = []
        while queue:
            n = queue.pop(0)
            if(n in visited):
                continue
            neighs = adj_list[n]
            visited.append(n)
            for i in neighs:
                queue.append(i)
        return sorted(visited)


if __name__ == "__main__":
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    print(Solution().countComponents(n, edges))
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    print(Solution().countComponents(n, edges))