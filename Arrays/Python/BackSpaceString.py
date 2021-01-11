"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty."""

class Solution:
    def backspaceCompare(self, S, T):
        S = self.dobackspace(S)
        T = self.dobackspace(T)
        return S==T
    def dobackspace(self,s):
        while ('#' in s):
            ind = s.index('#')
            if(ind ==0): 
                s = s[0:ind]+s[ind+1:]
            else:
                s = s[0:ind-1]+s[ind+1:]
            return s 
            

        return s
if __name__ == '__main__':
    S = "ab##" 
    T = "c#d#"
    S1 = "#a#c"
    T1 = "a##c"
    S2= "oi###mupo##rszty#s#xu###bxx##dqc#gdjz"
    S3="oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"
    ss = s2 = Solution().backspaceCompare(S2,S3)
    s = Solution().backspaceCompare(S,T)
    print(s)
    s2 = Solution().backspaceCompare(S1,T1)
    print(s2)