class Solution:
    def maxSubArrayNaive(self, nums):
        max_sum = -2**32
        curr_matrix = []
        for i in nums:
            new_matrix = curr_matrix + [i]
            if(sum(new_matrix)<0 and curr_matrix):
                max_sum = max(sum(curr_matrix),max_sum)
                curr_matrix = []
            elif(sum(new_matrix)<0):
                max_sum = max(sum(new_matrix),max_sum)
            else:
                curr_matrix = new_matrix[:]
                max_sum = max(sum(curr_matrix),max_sum)
        return max_sum

    def maxSubArray(self, nums):
        max_sum = -2**32
        curr_matrix = []
        curr_sum = 0
        for i in nums:
            new_sum = curr_sum+i
            if(new_sum<0):
                curr_sum = 0
                max_sum = max(new_sum,max_sum)
            else:
                max_sum = max(new_sum,max_sum)
                curr_sum = new_sum
        return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(Solution().maxSubArray(nums))