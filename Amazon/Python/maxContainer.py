"""Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.
"""
class Solution:
    def maxAreaBF(self, height):
        
        max_container = 0 
        for i in range(0,len(height)-1):
            for j in range(len(height)-1,i,-1):
                curr_height = height[i]
                area = (j-i)*min(curr_height,height[j])
                max_container = max(max_container,area)
        return max_container


    # The optimal solution is actually a two pointer 
    # approach
    def maxArea(self, height):
        
        max_container = 0 
        left = 0 
        right = len(height)-1
        
        while left<right:
            
            area = (right-left)* min(height[left],height[right])
            max_container = max(area,max_container)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return max_container
        

if __name__ == "__main__":
    inps = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(inps))