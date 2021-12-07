"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

"""

class Solution:
    
    def __init__(self):
        self.parents  = None
        self.rank = None
    
    def countComponents(self, n, edges):
        self.parents = list(range(n))
        self.rank = [0]*n
        
        for edge in sorted(edges):
            self.union(*edge)
            
        for edge in sorted(edges):
            self.union(*edge)
        
        return len(list(set(self.parents)))
            
            
    def find_parent(self,n):
        
        # if I'm not my own parent find my parent
        if(self.parents[n]!=n):
            
            # make my parent my parents parent
            self.parents[n] = self.find_parent(self.parents[n])
        
        return self.parents[n]
    def union(self,x,y):
        xr, yr = self.find_parent(x), self.find_parent(y)
        if self.rank[xr] < self.rank[yr]:
            self.parents[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parents[yr] = xr
        else:
            self.parents[yr] = xr
            self.rank[xr] += 1

if __name__ == "__main__":
    n = 6
    edges = [[0,1],[0,2],[2,5],[3,4],[3,5]]
    print(Solution().countComponents(n,edges))


