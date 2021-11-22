"""
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
"""



class Solution:
    def longestSubsequence(self, arr, difference):
        seen = {}
        for x in arr:     
            seen[x] = seen.get(x-difference, 0)+1
        return max(seen.values())
        

if __name__ == "__main__":
    arr = [1,5,7,8,5,3,4,2,1,-1]
    difference = -2
    print(Solution().longestSubsequence(arr,difference))