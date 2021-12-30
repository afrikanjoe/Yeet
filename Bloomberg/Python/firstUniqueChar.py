"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        
        c = Counter(s)
        indices = {}
        
        for i,r in enumerate(s):
            
            val = indices.get(r,None)
            if(val==None):
                indices[r] = i
            
            
        index = 2**32
        for key in c.keys():
            if(c[key]==1):
                index = min(index,indices[key])
                
        if(index==2**32):
            return -1
        else:
            return index

if __name__ == "__main__":
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))