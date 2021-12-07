"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""

class Solution:
    def uniquePathsBF(self, m, n):
        
        queue = [[(0,0)]]
        end = (m-1,n-1)
        count=0
        while queue:
            
            curr_list = queue.pop()
            top_node_x,top_node_y = curr_list[-1]
            
            if((top_node_x,top_node_y)==end):
                count+=1
                continue
                
            if((top_node_x+1)<m):
                new_list = curr_list[:] +[(top_node_x+1,top_node_y)]
                queue.append(new_list)
                
                
            if((top_node_y+1)<n):
                new_list2 = curr_list[:] +[(top_node_x,top_node_y+1)]
                queue.append(new_list2)
        return count


    def uniquePaths(self, m, n):
        arr = []
        for i in range(m):
            if(i==0):
                col = [1]*n
            else:
                col = [1] +(n-1)*[0]
            arr.append(col)
        
        
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[m-1][n-1]

if __name__ == "__main__":
    m= 23
    n = 12
    print(Solution().uniquePaths(m,n))

