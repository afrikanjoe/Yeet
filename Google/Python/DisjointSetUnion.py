"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.
"""

class Solution:
    
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [0] * 1001
        
        
    def find(self,x):
        
        if(self.par[x]!=x):
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        xp, yp = self.find(x), self.find(y)
        
        # get the ranks of the parents
        xp_rank, yp_rank = self.rnk[xp], self.rnk[yp] 
        
        # if they have the same parent then they are a redundant connection 
        if(xp == yp):
            return False
        
        # merging connecting components 
        elif(xp_rank>yp_rank):
            self.par[yp] = xp
        elif(yp_rank>xp_rank):
            self.par[xp] = yp
        # unconnected component
        else:
            self.par[yp] = xp
            self.rnk[xp]+=1
        return True
            
    def findRedundantConnection(self, edges):
        for edge in edges:
            if not self.union(*edge):
                return edge

if __name__ == "__main__":
 edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
 print(Solution().findRedundantConnection(edges))
            