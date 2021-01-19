"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        count = 0
        maxi =0 
        curr = []
        for i in s:
            if i in curr:
                ind = curr.index(i)
                curr = curr[ind+1:]+[i]
                count = len(curr)
            else:
                count+=1
                if(count>maxi):
                    maxi = count
                curr.append(i)
        return maxi


if __name__ == "__main__":
    inp = "asjrgapa"
    print(Solution().lengthOfLongestSubstring(inp))