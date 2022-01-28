"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.


"""

import heapq
class Solution:
    def lastStoneWeight(self, stones):
        
        heap = []
        
        for i in stones:
            heapq.heappush(heap,-i)
            
        
        while len(heap)>1:
            
            y = - heapq.heappop(heap)
            x = - heapq.heappop(heap)
            if(y==x):
                continue
            else:
                heapq.heappush(heap,-(y-x))
        
        if(not heap):
            return 0
        else:
            return -heap[0]