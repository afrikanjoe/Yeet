"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""




import heapq
class Solution:
    def removeDuplicates(self, nums):
        heap = []
        counts = {}
        for i in nums:
            if(counts.get(i,0)>1):
                continue
            else:
                counts[i] = counts.get(i,0)+1
                heapq.heappush(heap,i)
        
        index = 0 
        len_heap = len(heap)
        pops = len(nums) - len(heap)
        
        while heap:
            val = heapq.heappop(heap)
            nums[index] = val
            index+=1
            
        for i in range(pops):
            nums.pop()


class OptimalSolution:

    def removeDuplicates(self,nums):
        count=1 
        index = 0  
        prev = None
        while index < len(nums):
            if(nums[index]==prev):
                count+=1
                if(count>1):
                    nums.pop(index)
                    index-=1
            else:
                count=0 
                prev = nums[index]
            index+=1

if __name__ == "__main__":
    nums = [0,0,0,1,1,1,1,2,3,3]
    print(nums)
    OptimalSolution().removeDuplicates(nums)
    print(nums)