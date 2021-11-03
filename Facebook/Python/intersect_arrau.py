"""

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""

class Solution:
    def intersect(self, nums1, nums2):
        
        res = []
        if(len(nums1)<=len(nums2)):
            for i in nums1:
                if i in nums2:
                    res.append(i)
                    nums2.remove(i)
            
        else:
            for i in nums2:
                if i in nums1:
                    res.append(i)
                    nums1.remove(i)
        return res


if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1,nums2))
    