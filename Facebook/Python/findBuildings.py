"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Examples: 

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

"""

class Solution:
    def findBuildings(self, heights):
        if(not heights):
            return []
        views_from_the_six = [len(heights)-1]
        max_right = heights[len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            curr_height = heights[i]
            if(curr_height>max_right):
                views_from_the_six.insert(0,i)
                max_right = curr_height
        return views_from_the_six


if __name__ == "__main__":
    heights = [4,2,3,1]
    print(Solution().findBuildings(heights))
    heights = [4,3,2,1]
    print(Solution().findBuildings(heights))
    heights = [1,3,2,4]
    print(Solution().findBuildings(heights))
    heights = [2,2,2,2]
    print(Solution().findBuildings(heights))