"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

Optimal Solution: 

The idea behind this approach is as follows: If the cumulative sum up to two indices is the same, the sum of the elements lying in between those indices is zero. 
Extending the same thought further, if the cumulative sum up to two indices, say i and j is at a difference of k, sum[i] - sum[j] = k the sum of elements lying 
between indices i and j is k. Based on these thoughts, we make use of a hashmap mapmap which is used to store the cumulative sum up to all the indices possible along with t
he number of times the same sum occurs. We store the data in the form: (sum_i, no. of occurrences of sum_i)
We traverse over the array numsnums and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. 
If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum sum-k 
has occurred already, since it will determine the number of times a subarray with sum kk has occurred up to the current index. We increment the countcount by the same amount.

After the complete array has been traversed, the countcount gives the required result.





"""

class Solution:
    def subarraySumBF(self, nums, k):
        count = 0
        for i in range(1,len(nums)+1):
            for j in range(len(nums)-i+1):
                curr_arr = nums[j:j+i]
                curr_sum = sum(curr_arr)
                if(curr_sum==k):
                    count+=1
        return count

    def subarraySumMemoryIntensive(self, nums, k):
        queue = [[nums[i],i,i] for i in range(len(nums))]
        count=0
        visited = []
        while queue:
            curr_sum, start,end = queue.pop()
            if(curr_sum==k and [curr_sum,start,end] not in visited):
                count+=1
            else:
                if(start-1>=0):
                    new_sum = curr_sum+nums[start-1]
                    if(new_sum<=k):
                        queue.append([new_sum,start-1,end])
                if(end+1<len(nums)):
                    new_sum = curr_sum+nums[end+1]
                    if(new_sum<=k):
                        queue.append([new_sum,start,end+1])
            visited.append([curr_sum,start,end])
        return count

    # Cumulative Sum approach is kind of wild 
    def subarraySum(self, nums, k):
        cum_sum_dict = {0:1}
        curr_sum = 0 
        count = 0 
        for i in range(len(nums)):
            curr_sum+= nums[i]
            sumk = curr_sum - k 
            count+=cum_sum_dict.get(sumk,0)
            cum_sum_dict[curr_sum] = cum_sum_dict.get(curr_sum,0)+1 
        return count


if __name__ == "__main__":
    inp = [1,2,3,4,1,2,3,4]
    k = 5
    print(Solution().subarraySumBF(inp,k))
    print(Solution().subarraySumMemoryIntensive(inp,k))
    print(Solution().subarraySum(inp,k))