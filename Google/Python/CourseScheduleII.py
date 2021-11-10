"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        possible, top_sort = self.solutionPossible(numCourses,prerequisites)
        print(possible)
        if(possible):
            return top_sort
        else:
            return []
        
    def solutionPossible(self,numCourses, prerequisites):
        
        # adj_list 
        adj_list = {}
        
        
        # create a dictionary to store the in-degree of each of the nodes
        in_degree = {}
        for i in range(numCourses):
            in_degree[i] = 0
            
        # calculate the in_degree of each node
        for preq in prerequisites:
            in_degree[preq[0]] = in_degree[preq[0]] +1
            val = adj_list.get(preq[1],0)
            if(val==0):
                adj_list[preq[1]] = [preq[0]]
            else:
                val.append(preq[0])
                adj_list[preq[1]] = val
            
        queue = []
        for key in list(in_degree.keys()):
            if in_degree[key] ==0:
                queue.append(key)
        
        # go through the list and remove nodes one by 
        # one from the graph adding nodes with a new_indgree of zero 
        top_sort = []
        while queue:
            node = queue.pop(0)
            top_sort.append(node)
            neighs = adj_list.get(node,0)
            if(neighs!=0):
                for val in neighs:
                    in_degree[val] = in_degree[val]-1
                    if(in_degree[val]==0):
                        queue.append(val)
        return len(top_sort)==numCourses, top_sort
            
        