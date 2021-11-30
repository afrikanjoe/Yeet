"""
Given a string s, return the longest palindromic substring in s.
"""

from functools import lru_cache
class Solution:

    # this is a valid solution, though very slow, you can make it 
    # better with memoization
    @lru_cache(maxsize=None)
    def longestPalindrome(self, s):
        if(s==s[::-1]):
            return s
        elif(len(s)==1):
            return a
        else:
            last_index = len(s)-1
            rm_first = self.longestPalindrome(s[1:])
            rm_second = self.longestPalindrome(s[:last_index])
            if(len(rm_first)>len(rm_second)):
                return rm_first
            else:
                return rm_second


if __name__ == "__main__":
    s = "abbcccbbbcaaccbababcbcabca"
    print(Solution().longestPalindrome(s))