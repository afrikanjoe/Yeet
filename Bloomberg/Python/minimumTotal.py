"""
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""
from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle):
        
        def helper(row,index,count,triangle):
            if(row==len(triangle)-1):
                if(index+1)<len(triangle[row]):
                    return count + min(triangle[row][index],triangle[row][index+1])
                else:
                    return count + triangle[row][index]
            else:
                if(index+1)<len(triangle[row]):
                        return min(helper(row+1,index,count+triangle[row][index],triangle),helper(row+1,index+1,count+triangle[row][index+1],triangle))
                else:
                    return helper(row+1,index,count+triangle[row][index],triangle)

        return helper(0,0,0,triangle)


class OptimalSolution:
    def minimumTotal(self, triangle):
        
        @lru_cache(maxsize=None)
        def helper(row,col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(helper(row + 1, col), helper(row + 1, col + 1))
            return path
        return helper(0, 0)
            
if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(OptimalSolution().minimumTotal(triangle))