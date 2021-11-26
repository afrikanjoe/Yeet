"""In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input."""


class Solution:
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [0] * 1001
        
    def find(self, x):
        
        # if I'm not my own parent 
        if self.par[x] != x:
            print(x,self.par[x])
            # then make my parent my parent's parent, 
            # so this case is 1,2, 2,3 2's parent is 1
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        
        # if they have the same parent they're already connected
        if xr == yr:
            return False
        # make the parent of xr or yr the parent with the higher rank
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


    def findRedundantConnection(self, edges):
        for edge in edges:
            if not self.union(*edge):
                return edge


if __name__ == "__main__":
    edges = [[2,1],[3,4],[2,4],[3,5],[2,5]]
    print(Solution().findRedundantConnection(edges))