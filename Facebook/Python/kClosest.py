"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import heapq
import math
class Solution:
    def kClosest(self, points, k: int):
        heap = []
        res = []
        for pt in points:
            item = (self.compute_distance(pt),pt)
            heapq.heappush(heap,item)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        
    def compute_distance(self, pt):
        
        val = pt[0]**2 + pt[1]**2
        return math.sqrt(val)


if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(Solution().kClosest(points,k))
    points = [[1,3],[-2,2]]
    k = 1
    print(Solution().kClosest(points,k))
