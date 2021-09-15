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
        replace = True
        while replace: 
            st,en = self.match_braces(s)
            print(st,en)
            if(st>0):
                num,count = self.get_num(s,st)
                new_substr = num * s[st+1:en]
                s = s[0:st-count] + new_substr + s[en+1:]
            else: 
                replace = False 
            
        return s 
        
    


    def get_num(self,s,st):
        looping = True
        num = ''
        count = 0
        start = st-1
        while looping:
            if(s[start].isdigit()):
                num = s[start]+num
                count+=1
            else:
                looping = False
            start-=1
            


        return int(num),count 



    def match_braces(self,s):
        start = -1
        end = -1
        skip = 0 
        for i in range(len(s)):
            if(s[i]=='['):
                start = i 
                break

        for j in range(start+1,len(s)):
            if(s[j]=='['):
                skip +=1
            elif s[j]==']' and skip>0:
                skip-=1
            elif s[j]==']':
                end = j 
                break
        return start,end
            
            
        
if __name__== "__main__":
    inp = "3[a]2[bc]"
    print(Solution().decodeString(inp))

    inp = "3[a2[c]]"
    print(Solution().decodeString(inp))

    inp = "2[abc]3[cd]ef"
    print(Solution().decodeString(inp))

    inp = "abc3[cd]xyz"
    print(Solution().decodeString(inp))

    inp = "10[leetcode]"
    print(Solution().decodeString(inp))
