"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

class Solution:
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals)
        rooms = [intervals[0]]
        
        for i in intervals[1:]:
            added = False
            for room in rooms:
                if(i[0]>=room[1]):
                    added=True
                    rooms[rooms.index(room)] = i
                    break
            if(not added):
                rooms.append(i)
        return len(rooms)

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print(Solution().minMeetingRooms(intervals))