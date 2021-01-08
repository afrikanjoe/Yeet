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
            if(ind-1>=0):
                rem = s[ind-1]
                s= s.replace(rem,'').replace('#','',1)
        return s
if __name__ == '__main__':
    S = "ab##" 
    T = "c#d#"
    s = Solution().backspaceCompare(S,T)
    print(s)