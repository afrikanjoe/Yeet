"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m 
elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_real = len(nums1)
        if(n==0):
            return nums1
        elif(m==0):
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        else:
            
            
            
            start_index = m 
            while nums2:
                num2_val = nums2.pop(0)
                nums1[start_index] = num2_val
                curr_m = start_index
                previous_m = start_index-1
                while previous_m>=0:
                    if(nums1[curr_m]<nums1[previous_m]):
                        self.swap(nums1,curr_m,previous_m)
                        curr_m-=1
                        previous_m-=1
                    else:
                        break
                start_index+=1
                
                
            
            
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    Solution().merge(nums1,m,nums2,n)
    print(nums1)