import heapq 

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        heap = []
        profit = 0 
        orders_left = orders
        for i in inventory:
            heapq.heappush(heap,-i)
            
        
        while len(heap)>1 and orders_left>0:
            curr_val = - heapq.heappop(heap)
            heap_top = - heap[0]
            
            if((curr_val- heap_top)==0):
                orders_left-=1
                profit+=heap_top
                heapq.heappush(heap,-(curr_val-1))
            else:
                diff = curr_val- heap_top
                left = curr_val - diff + 1
                profit+= self.range_sum(left,curr_val)
                heapq.heappush(heap,-(curr_val-diff))
                orders_left-=diff
                
                
            
        
        # add the final sum 
        
        if(orders_left):
            left = ((-heap[0]) - orders_left )+1
            print(left)
            profit+= self.range_sum(left,-heap[0])
            print(profit)
        
        mod = (10**9 + 7)
        return profit  % mod
    
    
    def range_sum(self,left,right):
        return self.natural_sum(right) - self.natural_sum(left-1)
        
    def natural_sum(self,n):
        return int(n*(n+1)/2)
        