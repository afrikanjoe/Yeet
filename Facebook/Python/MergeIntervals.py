"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

class Solution:
    def merge(self, intervals):
        result = []
        intervals = sorted(intervals)
        queue = intervals[:]
        while len(queue)>1:
            int1 = queue.pop(0)
            int2 = queue.pop(0)
            if(int2[0]<=int1[1]):
                new_int = [min(int1+int2),max(int1+int2)]
                queue.insert(0,new_int)
            else:
                result.append(int1)
                queue.insert(0,int2)
        
        for i in queue:
            result.append(i)
        
        return result

if __name__ == "__main__":
    inp = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    print(Solution().merge(inp))
    inp = [[1,3],[1,4],[1,5],[15,18]]
    print(Solution().merge(inp))