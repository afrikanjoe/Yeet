"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.
"""



class Solution:
    def networkDelayTime(self, times,n,k):
        
        delays = [-1]*(n+1)
        delays[0] = 0 
        
        adj_list = {}
        for path in times:
            
            val = adj_list.get(path[0],[])
            val.append(path[1:])
            adj_list[path[0]] = val
            
        queue = [[k,0]]
        
        visited = []
        while queue:
            
            path = queue.pop(0)
            visited.append(path[0])
            if(delays[path[0]]==-1 or path[1]< delays[path[0]]):
                delays[path[0]] = path[1]
            neighs = adj_list.get(path[0],[])
            for n in neighs:
                new_n = [n[0],path[1]+n[1]]
                if(new_n[0] not in visited):
                    queue.append(new_n)
                elif(new_n[0] in visited and new_n[1]<delays[new_n[0]]):
                     queue.append(new_n)
        
        
        if(-1 in delays):
            return -1
        else:
            return max(delays)

if __name__ == "__main__":
    times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
    n = 3
    k = 2
    print(Solution().networkDelayTime(times,n,k))

            