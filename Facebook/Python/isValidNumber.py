"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

"""
class Solution:
    # cheating way
    def isNumberSimple(self, s):
        s = s.lower()
        try:
            if("inf" in s):
                return False
            s = float(s)
            return True
        except:
            return False


    def isNumber(self, s):
        s = s.lower()
        valid_chars = ["e","+","-","."]
        for i in range(10):
            valid_chars.append(str(i))
            
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        
        for i in range(len(s)):
            val = s[i]
            if(val not in valid_chars):
                return False
            elif(val.isnumeric()):
                seen_digit = True
            elif(val=="-" or val=="+"):
                if(i==0):
                    continue
                elif(s[i-1]=="e" and i+1<len(s) and s[i+1].isnumeric()):
                    continue
                else:
                    return False
            elif(val=="."):
                if(seen_dot or seen_exponent):
                    return False
                else:
                    seen_dot = True
            elif(val=="e"):
                if(seen_exponent):
                    return False
                elif(i-1>=0 and i+1<len(s)):
                    if(s[i-1].isnumeric() or s[i-1]=="." and (i-1)!=0):
                        seen_exponent = True
                    else:
                        return False
                else:
                    return False
        return seen_digit
            
        
        
if __name__ == "__main__":
    valids = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    invalids  = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    s = Solution()
    for i in valids:
        print(i,s.isNumber(i))
    for i in invalids:
        print(i,s.isNumber(i))