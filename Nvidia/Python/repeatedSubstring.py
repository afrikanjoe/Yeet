"""
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        count = 1
        orig = a
        if (len(set(a)) <len(set(b))):
            return -1
        while b not in a:
            count+=1
            a = orig * count
            if(count>10000):
                return -1
        return count

class OptimalSolution:
    def repeatedStringMatch(self,a,b):
        n = len(b) // len(a)
        
        if b in a * n: return n
        if b in a * (n + 1): return n + 1
        if b in a * (n + 2): return n + 2
        
        return -1