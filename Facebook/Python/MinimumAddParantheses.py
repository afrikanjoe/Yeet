"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""

class Solution:
    def minAddToMakeValid(self, s):
        count = 0 
        stack = []
        for char in s:
            if(char=="("):
                stack.append(char)
            else:
                if(len(stack)>0):
                    stack.pop()
                else:
                    count+=1
        count+= len(stack)
        return count

if __name__ == "__main__":
    s = "())"
    print(Solution().minAddToMakeValid(s))
    s = "((("
    print(Solution().minAddToMakeValid(s))
    s = "()))(("
    print(Solution().minAddToMakeValid(s))
