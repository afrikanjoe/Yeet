"""

Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, 
and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, 
end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination

"""

class Solution:

    def leadsToDestination(self, n, edges, source, destination):
        destination_in_path = True
        adj_matrix = {}
        
        for i in range(n):
            adj_matrix[i] = []
        for edge in edges: 
            adj_matrix[edge[0]].append(edge[1])
            
        queue = [[source]]
        visited = []
        while queue:
            n_list = queue.pop()
            if(n_list in visited):
                continue
            visited.append(n_list)
            top_node = n_list[-1]

            val = adj_matrix.get(top_node,[])
            if(len(val)==0):
                if(destination != n_list[-1]):
                    return False
            else:
                still_exploring = False
                for i in val: 
                    new_list = n_list[:]
                    if i not in new_list:
                        new_list.append(i)
                        still_exploring = True
                        queue.append(new_list)
                    else:
                        return False
                if(not still_exploring):
                    if(destination != n_list[-1]):
                        return False
        return True

        


if __name__ == "__main__":
    n = 3 
    edges = [[0,1],[0,2],[1,2]]
    source = 0 
    destination = 2

    print(Solution().leadsToDestination(n,edges,source,destination))

    n = 4
    edges = [[0,1],[0,3],[1,2],[2,1]]
    source = 0
    destination = 3

    print(Solution().leadsToDestination(n,edges,source,destination))

    n = 3
    edges = [[0,1],[1,1],[1,2]]
    source = 0
    destination = 2
    print(Solution().leadsToDestination(n,edges,source,destination))