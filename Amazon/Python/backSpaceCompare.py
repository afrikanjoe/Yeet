"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    def backspaceCompare(self, s, t):
        
        
        s_stack = []
        t_stack = []
        
        for i in s:
                if(i=="#" and len(s_stack)>0):
                    s_stack.pop()
                elif(i=="#"):
                    continue
                else:
                    s_stack.append(i)
                    
        for i in t:
                if(i=="#" and len(t_stack)>0):
                    t_stack.pop()
                elif(i=="#"):
                    continue
                else:
                    t_stack.append(i)
        return s_stack == t_stack

if __name__ == "__main__":
    s = "a##c"
    t = "#a#c"
    print(Solution().backspaceCompare(s,t))