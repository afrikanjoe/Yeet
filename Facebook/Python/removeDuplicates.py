"""
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
"""

class Solution:
    def removeDuplicatesSlow(self, s):
        prev = None
        while prev!=s:
            prev = s
            for i in range(len(s)-1):
                if(s[i]==s[i+1]):
                    s = s[0:i] + s[i+2:]
                    break
        return s

    def removeDuplicatesFast(self,s):
        stack = []
        for i in s:
            if(len(stack)>0 and stack[-1]==i):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)



if __name__=="__main__":
    inp = "abbaca"
    print(Solution().removeDuplicates(inp))
    inp2 = "azxxzy"
    print(Solution().removeDuplicates(inp2))