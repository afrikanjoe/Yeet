"""
I learned that if you want to detect a cycle in a graph you have to do a topological sort.
Sheesh this was a hard problem
https://algocoding.wordpress.com/2015/04/05/topological-sorting-python/

"""



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # create list for tracking indgrees of nodes
        in_degree = {}
        for i in range(numCourses):
            in_degree[i] = 0
        
        adj_list = {}
        # count the in degrees
        for preq in prerequisites:
            
            val = adj_list.get(preq[1],0)
            if(val==0):
                adj_list[preq[1]] = [preq[0]]
            else:
                val.append(preq[0])
                adj_list[preq[1]] = val
            
            in_degree[preq[0]]=in_degree[preq[0]]+ 1
        
        # add all the nodes with an indegree of zero
        queue = []
        for key in list(in_degree.keys()):
            if in_degree[key]==0:
                queue.append(key)
                
        # List to store topological sort of graph
        top_sort = []
        while queue:
            node = queue.pop()
            top_sort.append(node)
            neighs = adj_list.get(node,0)
            if(neighs==0):
                continue
            else:
                for n in neighs:
                    in_degree[n] = in_degree[n] -1
                    if(in_degree[n]==0):
                        queue.append(n)
        return len(top_sort)==numCourses
        
      
                