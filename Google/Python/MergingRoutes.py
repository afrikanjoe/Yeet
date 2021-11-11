"""
We have a set of routes where QA reported issues. However, a lot of these routes go over the same road segments. Based on the reports, we want to create the _minimum_ set of test routes so that every road segment driven by QA is covered.

Example:
    route1: A -> B -> C
    route2: M -> B -> C -> N
    route3: Q -> B -> C -> D
    route4: K -> L
    route5: D -> K -> X
    minimum set of routes to cover every road segment: A -> B -> C -> D -> K -> L, M -> B -> C -> N, Q -> B -> C -> D -> K -> X

    - Assume fully connected graph
    - Assume all these are directed edges
    - Assume there are no cycles in the graph
    - Assume there are no two paths from any node 1 to node 2; For example, you won't have B -> C -> D and B -> P -> D - since that would create two paths from B to D

    Code: input and output should be list of strings; In: ["ABC", "MBCN", "QBCD", "KL", "DKX"] Out: ["ABCDKL", "MBCN", "QBCDKX"]
"""

class Solution:

    def merge_routes(self,routes):

        # create the adjacency matrix and compute the incount
        adj_matrix  = {}
        in_degree = {}
        for route in routes:
            for node in range(len(route)-1):
                val = adj_matrix.get(route[node],[])
                in_degree[route[node+1]] = in_degree.get(route[node+1],0)+1
                if(len(val)==0):
                    adj_matrix[route[node]] = [route[node+1]]
                elif(route[node+1] not in val):
                    adj_matrix[route[node]].append(route[node+1])

        # add all the nodes to a queue for the exploration
        queue = []
        for node in list(adj_matrix.keys()):
            in_count = in_degree.get(node,0)
            if(in_count==0):
                queue.append([node])

        visited_end_nodes = []
        paths = []
        while queue:
            curr_path = queue.pop()
            last_node = curr_path[-1]
            neighbors = adj_matrix.get(last_node,[])
            if(len(neighbors)==0):
                visited_end_nodes.append(last_node)
                paths.append(curr_path)
            else:
                end_nodes_available = False
                for n in neighbors:
                    new_path = curr_path[:]
                    if(n not in visited_end_nodes):
                        new_path.append(n)
                        queue.append(new_path)
                        end_nodes_available =  True
                        break
                if(not end_nodes_available):
                    paths.append(curr_path)

        paths = ["".join(i) for i in paths]
        return paths
                

            


        

        






if __name__ == "__main__":
    inp = ["ABC", "MBCN", "QBCD", "KL", "DKX","ECN"]
    print(Solution().merge_routes(inp))
    