"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

"""

class Solution:
    def romanToInt(self, s):
        num = 0 
        index = 0 
        n = len(s)
        while index<n:
            if(s[index]== "I"):
                if(index+1<n):
                    if(s[index+1]=="X"):
                        num+=9
                        index+=1
                    elif(s[index+1]=="V"):
                        num+=4
                        index+=1
                    else:
                        num+=1
                else:
                    num+=1
            elif(s[index]== "X"):
                if(index+1<n):
                    if(s[index+1]=="L"):
                        num+=40
                        index+=1
                    elif(s[index+1]=="C"):
                        num+=90
                        index+=1
                    else:
                        num+=10
                else:
                    num+=10
            elif(s[index]=="C"):
                if(index+1<n):
                    if(s[index+1]=="D"):
                        num+=400
                        index+=1
                    elif(s[index+1]=="M"):
                        num+=900
                        index+=1
                    else:
                        num+=100
                else:
                    num+=100
            elif(s[index]=="V"):
                num+=5
            elif(s[index]=="L"):
                num+=50
            elif(s[index]=="D"):
                num+=500
            elif(s[index]=="M"):
                num+=1000
            index+=1
        return num 

if __name__ == "__main__":
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
    s = "LVIII"
    print(Solution().romanToInt(s))
