"""

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.


Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

"""

class Solution: 
    def sortColors(self, a):
            """
            Do not return anything, modify nums in-place instead.
            """
            arr_size = len(a)
            lo = 0
            hi = arr_size - 1
            mid = 0
            while mid <= hi: 
                if a[mid] == 0: 
                    a[lo], a[mid] = a[mid], a[lo] 
                    lo = lo + 1
                    mid = mid + 1
                elif a[mid] == 1: 
                    mid = mid + 1
                else: 
                    a[mid], a[hi] = a[hi], a[mid]  
                    hi = hi - 1


if __name__ == "__main__":
    inp = [2,0,2,1,1,0]
    Solution().sortColors(inp)
    print(inp)