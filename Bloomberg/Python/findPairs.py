"""
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).

"""

from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.c = Counter(self.nums2)
        
    def add(self, index: int, val: int) -> None:
        
        old_val  = self.nums2[index]
        new_val  = self.nums2[index] + val
        self.c[old_val]-=1
        self.c[new_val] = self.c.get(new_val,0)+1
        self.nums2[index]+=val

    def count(self, tot: int) -> int:
        count = 0
        for i in self.nums1:
            
            diff = tot - i 
            val = self.c.get(diff,0)
            count+=val
        return count
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)