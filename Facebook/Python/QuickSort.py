"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, 
respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums,0,len(nums)-1)
        
        
    def quickSort(self, arr,left,right):
        index = self.partition(arr,left,right)
        
        if(left<index-1):
            self.quickSort(arr,left,index-1)
        if(index<right):
            self.quickSort(arr,index,right)
            
        
    def partition(self,arr,left,right):
        
        # mid 
        mid = int((left+right)/2)
        pivot_val = arr[mid]
        
        while left<=right:
            
            # find the first left value that's out of place
            while arr[left]<pivot_val:
                left+=1
                
            # find the first left value that's out of place
            while arr[right]>pivot_val:
                right-=1
                
            if(left<=right):
                self.swap(arr,left,right)
                right-=1
                left+=1
        return left
                
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp 
        