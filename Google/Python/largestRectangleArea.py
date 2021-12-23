"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

class Solution:
    def largestRectangleArea(self, heights):
        
        
        left_indices = [-1] * len(heights)
        right_indices  = [len(heights)]*len(heights)
        
        stack  = []
        
        for i in range(len(heights)):
            # get the current value of the item in heights
            curr_val = heights[i]
    
            if(stack):
                
                
                # get the value of the item at the index on the top of the
                # stack
                top_of_stack = heights[stack[-1]]
                while stack:
                    
                    #print(i,curr_val,top_of_stack,stack)
                    
                    # if the item here is larger than the item on the top of the stack
                    # update the right index of the item at the top of the stack 
                    # to be this index, remove it from the stack, and add the new index
                    if(curr_val<top_of_stack):
                        right_indices[stack[-1]] = i
                        #left_indices[i] = stack[-1]
                        stack.pop()
                    # if it's larger then set the left index of the to be the item on top of the stack
                    elif(curr_val>=top_of_stack):
                        left_indices[i] = stack[-1]
                        break
                    if(stack):
                        top_of_stack = heights[stack[-1]]
                stack.append(i)
            else:
                stack.append(i)
        
        
        max_area = 0 
        
        for i in range(len(heights)):
            rect = heights[i]
            
            width = (right_indices[i]-left_indices[i]-1)
            max_area = max(max_area,width*rect)
        
        return max_area

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights))
