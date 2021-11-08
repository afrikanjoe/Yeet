"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.
"""

class Solution:
    
    
    def __init__(self):
        self.results = []
    def removeInvalidParentheses(self, s):
        
        if(")" not in s and "(" not in s):
            return [s]
        ans = []
        valid, invalid, indexes = self.is_valid(s)
        if(valid):
            return [s]
        for char in invalid:
            if(char == ")"):
                search_indexes = indexes["closed"]
            else:
                search_indexes = indexes["open"]
            for j in search_indexes:
                curr_str = str(s)
                curr_str = curr_str[0:j]+curr_str[j+1:]
                cvalid, cinvalid, cindexes = self.is_valid(curr_str)
                if(len(invalid)>1):
                    other_sols = self. removeInvalidParentheses(curr_str)
                    for i in other_sols:
                        if(i not in ans and len(i)==(len(s)-len(invalid))):
                            ans.append(i)
                #print(cvalid,curr_str)
                if(cvalid and curr_str not in ans):
                    ans.append(curr_str)
        if(len(ans)==0):
            return [""]
        return ans
                
    def is_valid(self,inp_str):
        parentheses_indexes = {}
        invalid_parentheses = []
        stack = []
        valid = True
        for i in range(len(inp_str)): 
            if(inp_str[i] == "("):
                stack.append(inp_str[i])
                val = parentheses_indexes.get("open",0)
                if(val != 0):
                    val.append(i)
                    parentheses_indexes["open"] = val
                else:
                    parentheses_indexes["open"] = [i]
            elif(inp_str[i] == ")"):
                if(len(stack)>0):
                    stack.pop(0)
                else:
                    valid = False
                    invalid_parentheses.append(inp_str[i])
                val = parentheses_indexes.get("closed",0)
                if(val != 0):
                    val.append(i)
                    parentheses_indexes["closed"] = val
                else:
                    parentheses_indexes["closed"] = [i]
            else:
                continue
                    
        while stack:
            valid = False
            invalid_parentheses.append(stack.pop())
        return valid,invalid_parentheses,parentheses_indexes
            
                    
        
        


if __name__ == "__main__":
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))
    s = "(a)())()"
    print(Solution().removeInvalidParentheses(s))
    s = ")("
    print(Solution().removeInvalidParentheses(s))
    s= "()))"
    print(Solution().removeInvalidParentheses(s))