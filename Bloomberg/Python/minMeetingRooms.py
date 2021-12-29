"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

class Solution:
    def minMeetingRooms(self, intervals):
        
        rooms = []
        intervals = sorted(intervals)
        
        for i in intervals:
            added = False
            for j in range(len(rooms)):
                intv = rooms[j]
                if(i[0]>=intv[1]):
                    rooms[j] = i 
                    added = True
                    break
            if(not added):
                rooms.append(i)
        return len(rooms)

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print(Solution().minMeetingRooms(intervals))