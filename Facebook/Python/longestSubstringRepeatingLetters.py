"""
Given a string s, find the length of the longest substring without repeating characters.


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        letters = set(s)
        max_len = len(letters)
        for i in range(max_len,0,-1):
            for j in range(len(s)-i+1):
                if len(set(s[j:j+i]))==i:
                    return i 
        return 0

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))