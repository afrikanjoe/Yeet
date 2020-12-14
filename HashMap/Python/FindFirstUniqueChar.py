"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""




class Solution:
    @staticmethod
    def firstUniqChar(s):
        count ={}
        very_large = (2**32 -1)
        val =  very_large
        for i in s:
            count[i]=count.get(i,0)+1
        for i in count.keys():
            if(count[i]==1):
                val = min(s.index(i),val)
        if(val==very_large):
            return -1
        else:
            return val


if __name__=="__main__":
    inp = "leetcode"
    print(Solution.firstUniqChar(inp))