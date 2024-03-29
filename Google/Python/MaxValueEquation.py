"""

You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, 
where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Example
Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. 
Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
"""

class Solution:
    def findMaxValueOfEquation(self, points, k):
        max_val = -1e9
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                
                pt1 = points[i]
                pt2 = points[j]
                
                if(abs(pt1[0]-pt2[0])<=k):
                    val = abs(pt1[0]-pt2[0]) +pt1[1]+pt2[1]
                    max_val = max(val,max_val)
                else:
                    break
        return max_val


if __name__ == "__main__":
    pts = [[1,3],[2,0],[5,10],[6,-10]]
    k = 1
    print(Solution().findMaxValueOfEquation(pts,k))
    pts = [[0,0],[3,0],[9,2]]
    k = 3
    print(Solution().findMaxValueOfEquation(pts,k))
