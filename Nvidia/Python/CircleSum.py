"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city 
are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

"""

class Solution:
    def findCircleNum(self, isConnected):
        
        adj_list = {}
        for i in range(len(isConnected)):
            row = isConnected[i]
            val = []
            for j in range(len(row)):
                if(i==j):
                    continue
                if(isConnected[i][j]):
                    val.append(j)
            adj_list[i] = val
        queue = [[i] for i in range(len(isConnected))]
        
        paths = []
        visited = []
        while queue:
            
            path = queue.pop(0)
            # if(path[-1] in visited):
            #     continue
            visited.append(path[-1])
            added = False
            
            new_path = path[:]
            for node in path:
                neighs = adj_list.get(node)
                for n in neighs:
                    if n not in new_path:
                        added = True
                        new_path.append(n)
                        visited.append(n)
            if(not added):
                if(path not in paths):
                    paths.append(path)
            else:
                queue.append(sorted(new_path))
        print(paths)
        return len(paths)

if __name__ == "__main__":
    connects = [[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,1,1,1,0],[0,0,1,1,0,0],[0,0,1,0,1,0],[0,0,0,0,0,1]]
    print(Solution().findCircleNum(connects))
            
            