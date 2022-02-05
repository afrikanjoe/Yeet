"""

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

"""

class Solution:
    def findMaxLength(self, nums):
        
        
        count_dict = {0:-1}
        count = 0
        max_length = 0 
        for i in range(len(nums)):
            if(nums[i]):
                count +=1
            else:
                count -=1
            if count_dict.get(count,-2)>=-1:
                max_length = max(max_length,i-count_dict[count])
            else:
                count_dict[count] = i
        return max_length

if __name__ == "__main__":
    nums = [0,1]
    print(Solution().findMaxLength(nums))