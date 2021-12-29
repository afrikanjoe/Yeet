"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n):
        
        s = list("()"*n)
        
        visited = []
        ans  = []
        queue = [s]
        while queue:
            
            ls = queue.pop()
            visited.append(ls)
            for i in range(1,len(s)):
                new_ls = ls[:]
                self.swap(new_ls,0,i)
                valid = self.is_valid(new_ls)
                if(new_ls not in visited and not valid):
                    queue.append(new_ls)
                elif(valid):
                    if "".join(new_ls) not in ans:
                        ans.append("".join(new_ls))
        return ans
                    
                
    
    def is_valid(self,s):
        
        stack = []
        for i in s:
            if(i=="("):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                else:
                    stack.pop()
        if(stack):
            return False
        return True
                
        
        
    def swap(self,arr,i,j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        

if __name__== "__main__":
    n= 5
    print(Solution().generateParenthesis(n))
    
        