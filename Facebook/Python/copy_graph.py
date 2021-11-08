"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(not node):
            return 

        root = Node(node.val)
        queue = [node]
        new_node_dict= {root.val:root}
        visited =[]
        while queue:
            curr_node = queue.pop()
            neighbors = []
            for n in curr_node.neighbors:
                if(n not in visited):
                    queue.append(n)
                new_node = new_node_dict.get(n.val,None)
                if(new_node==None):
                    new_node = Node(n.val)
                new_node_dict[new_node.val] = new_node
                neighbors.append(new_node)
                    
                   
            new_node_dict[curr_node.val].neighbors = neighbors
            visited.append(curr_node)
                
        return root
        
    
    def test_dfs(self,root):
        queue = [root]
        visited = [] 
        while queue:
            curr_node=queue.pop(0)
            if(curr_node in visited):
                continue
            visited.append(curr_node)
            print(curr_node.val)
            for i in curr_node.neighbors:
                if(i not in visited):
                    queue.append(i)
                    
        
        