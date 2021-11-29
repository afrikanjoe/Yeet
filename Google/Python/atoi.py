"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary 
(from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        
        # remove whitespace 
        s = self.passwhitespace(s)
        negative,s = self.determinesign(s)
        num = ""
        for i in s:
            if(i.isnumeric()):
                num=num+i
            else:
                break
        if(not num):
            return 0
        else:
            if(negative):
                return max(-(2**31),-int(num))
            else:
                return min((2**31)-1,int(num))
    
    
    def passwhitespace(self,s):
        if(not s):
            return s
        index = 0 
        for i in range(len(s)):
            if(s[i]==" "):
                index = i+1 
            else:
                break
        return s[index:]
    def determinesign(self,s):
        if(not s):
            return False,s
        if(s[0]=='-'):
            return True,s[1:]
        elif(s[0]=='+'):
            return False,s[1:]
        else:
            return False,s
                