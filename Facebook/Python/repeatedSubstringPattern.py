import collections

class Solution:
    def repeatedSubstringPatternBF(self, s: str) -> bool:
        
        count_dict = collections.Counter(s)
        chars = list(set(s))
        search_len = len(count_dict.keys())
        if(len(s)==0):
            return False
        elif(len(s)==1):
            return False
        else:
            for i in range(search_len,len(s)):
                for j in range(0,len(s)-i+1):
                    substr = s[j:j+i]
                    mult = int(len(s)/len(substr))
                    substr = substr*mult
                    if(substr == s):
                        return True
            return False

    # turns out the answer was very simple
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length):
            repeated_sub_string = s[:i] * (length // i)
            if repeated_sub_string == s:
                return True
        return False


if __name__ == "__main__":
    inp = "abcabcabcabc"
    print(Solution().repeatedSubstringPatternBF(inp))
    inp = "aba"
    print(Solution().repeatedSubstringPatternBF(inp))