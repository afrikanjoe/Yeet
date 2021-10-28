"""
You are given an m x n integer matrix points (0-indexed). 
Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. 
Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. 
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), 
picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
"""



class Solution:
    def maxPoints(self, points):
        
        queue = []
        max_val =-1e9
        m = len(points)
        n = len(points[0])
        for i in range(n):
            queue.append((points[0][i],[(0,i)]))
            
            
        while queue:
            
            curr_item = queue.pop(0)
            if(len(curr_item[1])==m):
                max_val = max(max_val,curr_item[0])
                continue
                
            val = curr_item[0]
            index_list = curr_item[1]
            last_index = index_list[-1]
            
            for j in range(last_index[0]+1,m):
                for k in range(0,n):
                    curr_index_list = index_list[:]
                    curr_index_list.append((j,k))
                    curr_val = val + points[j][k] - abs(last_index[1]-k)
                    queue.append((curr_val,curr_index_list))
        return max_val
            
if __name__ == "__main__":
    points = [[1,2,3],[1,5,1],[3,1,1]]
    print(Solution().maxPoints(points))
    points = [[1,5],[2,3],[4,2]]
    print(Solution().maxPoints(points))