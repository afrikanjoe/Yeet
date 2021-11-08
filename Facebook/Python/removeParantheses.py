"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.
"""

class Solution:
    def removeInvalidParentheses(self, s):
        left = 0 
        right = 0
        self.result = {}
        
        # First, we find out the number of misplaced left and right parentheses.
        for char in s: 

            # record a left bracket 
            if(char == '('):
                left +=1
            elif(char == ')'):

                # if we don't have a matching left, then this is a misplaced right
                right = right + 1 if left == 0 else right

                # decrement count of left parantheses because we have found a right 

                left = left -1 if left>0 else left

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        self.recurse(s, 0, 0, 0, left, right, [])
        return list(self.result.keys())
        
    
    def recurse(self,s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    self.result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    self.recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])    

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    self.recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    self.recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    self.recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                    

        
            
            
    

if __name__ == "__main__":
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))
    s = "(a)())()"
    print(Solution().removeInvalidParentheses(s))
    s = ")("
    print(Solution().removeInvalidParentheses(s))
    s= "()))"
    print(Solution().removeInvalidParentheses(s))

    s= "()(("
    print(Solution().removeInvalidParentheses(s))