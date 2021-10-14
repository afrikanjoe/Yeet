"""
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are 
considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
"""

class Solution: 
    def numberOfWays(self, arr, k):
        # Write your code here
        #  two pass, this double counts but is a genius method 
        count = 0
        count_dict = {}
        for i in arr:
            count_dict[i] = count_dict.get(i,0)+1
        # Initialize the list 
        for i in range(len(arr)):
            count+= count_dict.get(k-arr[i],0)
            if(k-arr[i] == arr[i]):
                count-=1
        return count // 2

if __name__ == "__main__":
    k = 6
    arr = [1, 2, 3, 4, 3]
    print(Solution().numberOfWays(arr,k))

    k = 6
    arr = [1, 5, 3, 3, 3]
    print(Solution().numberOfWays(arr,k))


