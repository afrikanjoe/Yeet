"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals 
still does not have any overlapping intervals (merge overlapping intervals if necessary).

"""

class Solution:
    def insert(self, intervals, newInterval):
        
        intervals.append(newInterval)
        intervals = sorted(intervals)
        
        merged_intervals = []
        
        while len(intervals)>1:
            
            interval1 = intervals.pop(0)
            
            interval2 = intervals.pop(0)
                       
            # they overlap
            if(interval2[0]<=interval1[1]):
                new_interval = [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]
                intervals = [new_interval] + intervals
            else:
                merged_intervals.append(interval1)
                intervals = [interval2] + intervals
        
        if(intervals):
            merged_intervals.append(intervals.pop())
        return merged_intervals

if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    print(Solution().insert(intervals,newInterval))


    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(Solution().insert(intervals,newInterval))