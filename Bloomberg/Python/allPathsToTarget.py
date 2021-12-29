"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).
"""

class Solution:
    def allPathsSourceTarget(self, graph):
        
        adj_list = {}
        
        for i in range(len(graph)):
            
            ls = graph[i]
            for j in ls:
                
                ns = adj_list.get(i,[])
                ns.append(j)
                adj_list[i] = ns
        
        paths = []
        queue = [[0]]
        
        while queue:
            
            path = queue.pop()
            top_node = path[-1]
            if(top_node==len(graph)-1):
                paths.append(path)
            
            ns = adj_list.get(top_node,[])
            for n in ns:
                
                if n not in path:
                    new_path = path + [n]
                    queue.append(new_path)
                    
        return paths

if __name__ == "__main__":
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(Solution().allPathsSourceTarget(graph))
        