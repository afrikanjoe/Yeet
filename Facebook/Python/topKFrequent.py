"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

import heapq
class Solution:
    def topKFrequent(self, nums, k):
        count_dict = {}
        heap = []
        res = []
        for i in nums:
            count_dict[i] = count_dict.get(i,0)+1
            heapq.heappush(heap,(-count_dict[i],i))
        
        while len(res)<k:
            top = heapq.heappop(heap)
            if(top[1] not in res):
                res.append(top[1])
        return res

    def topKFrequentFaster(self,nums,l):
        count_dict = {}
        heap = []
        res = []
        for i in nums:
            count_dict[i] = count_dict.get(i,0)+1
        count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1],reverse=True))
        for i in list(count_dict.keys())[:k]:
            res.append(i)
        return res

if __name__ == "__main__":
    inp = [1,2,1,2,1,2,3,3,3,1,3,3,3,3,3]
    k = 3
    print(Solution().topKFrequent(inp,k))
