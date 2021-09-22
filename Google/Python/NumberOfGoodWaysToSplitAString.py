"""
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number 
of distinct letters in p and q are the same. Return the number of good splits you can make in s.
"""

class Solution:
    def numSplitsBF(self, s):
        good_splits = 0
        for i in range(0, len(s)):
            left = set(s[0:i+1])
            right = set(s[i+1:])
            if(len(left)==len(right)):
                good_splits+=1
        return good_splits

    def numSplits(self, s: str) -> int:
        right_char_dict = {}
        left_char_set = set()
        good_splits =0
        # create the hashmap that will aid in checking for goodsplits
        for char in s:
            right_char_dict[char] = right_char_dict.get(char,0)+1
        for char in s:
            right_char_dict[char] = right_char_dict[char] -1
            if(right_char_dict[char]==0):
                del  right_char_dict[char]
            left_char_set.add(char)
            if(len(right_char_dict.keys())==len(left_char_set)):
                good_splits+=1
        return good_splits


if __name__=="__main__":
    inp = "acbadbaada"
    print(Solution().numSplits(inp))
