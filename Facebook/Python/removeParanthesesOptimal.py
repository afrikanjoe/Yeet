"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.
"""

class Solution:
    def removeInvalidParentheses(self, s):
        self.ans = []
        self.minMoves = float('inf')
        
        def rec(s, count):
            # if we've already found a better one no need to continue searching
            if not s or count > self.minMoves:
                return

            # otherwise see if it's valid and add it to the cache
            elif self.isValid(s):
                if count == self.minMoves:
                    self.ans.append(s)
                else:
                    self.minMoves = count
                    self.ans = [s]
            
            for i in range(len(s)):
                if s[i] in '()':
                    # remove one character each time
                    rec(s[:i] + s[i+1:], count+1)
                    
        rec(s, 0)
        return [''] if not self.ans else list(set(self.ans))
            
            
    def isValid(self, s):
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == '(': l += 1
            elif s[i] == ')': r += 1
                
            if r > l: return False
            
        return r == l

if __name__ == "__main__":
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))
    s = "(a)())()"
    print(Solution().removeInvalidParentheses(s))
    s = ")("
    print(Solution().removeInvalidParentheses(s))
    s= "()))"
    print(Solution().removeInvalidParentheses(s))