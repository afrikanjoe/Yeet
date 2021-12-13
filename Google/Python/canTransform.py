"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either 
replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". 
Given the starting string start and the ending string end, 
return True if and only if there exists a sequence of moves to transform one string to the other.
"""

class Solution:
    def canTransform(self, start, end):
        queue = [start]
        
        visited = []
        while queue:
            curr_str = queue.pop()
            if(curr_str==end):
                return True
            visited.append(curr_str)
            rx_ = curr_str.replace("RX","XR",1)
            lx_ = curr_str.replace("XL","LX",1)
            if(rx_ not in visited):
                queue.append(rx_)
            if(lx_ not in visited):
                queue.append(lx_)
        return False


if __name__ == "__main__":
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    print(Solution().canTransform(start,end))