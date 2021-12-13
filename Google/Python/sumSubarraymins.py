"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 109 + 7.
"""
class Solution:
    def sumSubarrayMins(self, arr):
        
        mins = []
        for i in range(1,len(arr)+1):
            for j in range(0,len(arr)-i+1):
                mins.append(min(arr[j:j+i]))
        return sum(mins)%(10**9 + 7)

if __name__ == "__main__":
    arr = [11,81,94,43,3]
    print(Solution().sumSubarrayMins(arr))