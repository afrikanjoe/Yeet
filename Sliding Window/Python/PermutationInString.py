"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.
"""


class Solution:
    def checkInclusion(self, s1, s2):
        ls1 = len(s1)
        ls2 = len(s2)
        test = sorted(s1)
        for i in range(ls2-ls1+1):
            if(test==sorted(s2[i:i+ls1])):
                return True
        return False

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1,s2))