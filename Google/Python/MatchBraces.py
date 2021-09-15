"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

Example: "3[a]2[bc]"
Output: "aaabcbc"
"""

class Solution:
    def decodeString(self, s):
        st,en = self.match_braces(s)
        if(st>0):
            num = st-1
        print(s[st+1:en])
        
    
    def match_braces(self,s):
        start = -1
        end = -1
        for i in range(len(s)):
            if(s[i]=='['):
                start = i 
                break
        for i in range(len(s)-1,-1,-1):
            if(s[i]==']'):
                end = i 
                break
        return start,end
            
            
        
if __name__== "__main__":
    inp = "3[a]2[bc]"
    print(Solution().decodeString(inp))
