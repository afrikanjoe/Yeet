"""

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

"""


class Solution:
    def removeOuterParentheses(self, s):
        indices = self.findIndices(s)
        return_str = ""
        for tup in indices:
            return_str = return_str+ s[tup[0]+1:tup[1]]
        return return_str




    def findIndices(self,s):
        adding = False 
        start = None 
        split_indices = []
        skip = 0
        for i in range(len(s)): 
            if(not adding and s[i]=='('):
                starting = i 
                adding = True
            elif(s[i]=='('):
                skip+=1
            elif(skip>0 and s[i]==')'):
                skip-=1
            else:
                adding = False 
                split_indices.append((starting,i))
        return split_indices



if __name__ == "__main__":
    s = "(()())(())(()(()))"
    print(Solution().removeOuterParentheses(s))
    s = "(()())(())"
    print(Solution().removeOuterParentheses(s))
    s = "()()"
    print(Solution().removeOuterParentheses(s))