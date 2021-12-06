"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""



class Solution:
    def longestCommonPrefix(self, strs):
        
        prefix = ""
        word1 = strs[0]
        
        min_len = 2**32
        for st in strs:
            if(len(st)<min_len):
                min_len = min(min_len,len(st))
                word1 = st
        
        for l in range(1,min_len+1):
            
            pref = word1[:l]
            valid = True
            for st in strs:
                if(st[:l]!= pref):
                    valid = False
                    break
            if(valid):
                prefix = pref
        return prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))