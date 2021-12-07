"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        
        for row in matrix:
            if(self.binary_search(row,0,len(row)-1,target)):
                return True
        return False
        
    
    
    def binary_search(self,nums,start,end,target):
        
        while start<=end:
            
            mid = (start + end)>>1
            if(nums[mid]==target):
                return True
            elif(nums[mid]>target):
                end = mid -1
            else:
                start = mid+1
        return False
        

if __name__ == "__main__":
    arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(Solution().searchMatrix(arr,target))