"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
"""

class Solution:
    def minRemoveToMakeValid(self, s):
        
        stack = []
        remove_stack =[]
        for i in range(len(s)):
            char = s[i]
            if(char=="("):
                stack.append((i,char))
            elif(char==")"):
                
                if(len(stack)==0):
                    remove_stack.append(i)
                else:
                    stack.pop()
        
        for i in stack:
            remove_stack.append(i[0])
            
            
        return_str = ""
        for i in range(len(s)):
            char = s[i]
            if(i not in remove_stack):
                return_str = return_str + char
        return return_str


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(Solution().minRemoveToMakeValid(s))
    s = "a)b(c)d"
    print(Solution().minRemoveToMakeValid(s))
    s = "))(("
    print(Solution().minRemoveToMakeValid(s))
    s = "(a(b(c)d)"
    print(Solution().minRemoveToMakeValid(s))