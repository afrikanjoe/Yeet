

class Solution:

    # This O(m+n log (m+n))
    def findMedianSortedArrays(self, nums1, nums2]):
        nums1 = nums1 + nums2
        nums1 = sorted(nums1)
        
        mid = (0 + len(nums1)-1)>>1
        if(len(nums1)%2==0):
            return (nums1[mid]+nums1[mid+1])/2
        else:
            return nums1[mid]