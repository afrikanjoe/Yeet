"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

"""



from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        indices = []
        c1 = Counter(p)
        for i in range(0,len(s)-len(p)+1):
            c2 = Counter(s[i:i+len(p)])
            if(c1==c2):
                indices.append(i)
        return indices

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s,p))