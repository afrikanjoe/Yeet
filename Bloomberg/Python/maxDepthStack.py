"""

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

"""

class Solution:
    def maxDepth(self, s):
        
        stack_count = 0 
        stack = []
        
        for i in s:
            if(i=="("):
                stack.append("(")
                stack_count = max(stack_count,len(stack))
            elif(i==")"):
                stack.pop()
        return stack_count

if __name__ == "__main__":
    s = "(1+(((2)))+(((3))))"
    print(Solution().maxDepth(s))

