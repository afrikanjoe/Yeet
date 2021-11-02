"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class Solution:
    def validPalindromeBF(self, s):
        for i in range(len(s)):
            temp = s[0:i] + s[i+1:]
            if(temp==temp[::-1]):
                return True
        return False
    
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        count = 0 # count > 1 return False
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                s1 = s[left+1: right+1]
                s2 = s[left: right]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True

if __name__ == "__main__":
    inp = "tebbem"
    print(Solution().validPalindrome(inp))
    inp = "abca"
    print(Solution().validPalindrome(inp))