"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

I'll take it 198 / 200 test cases passed.

Example
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

"""


class Solution:
    def maxProfit(self, prices):
        
        adj_matrix = {}
        for i in range(len(prices)):
            adj_matrix[i] = [i]
        
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                if prices[i]<prices[j]:
                    val = adj_matrix[i]
                    val.append(j)
                    adj_matrix[i] = val
        
        queue = []
        for key in adj_matrix:
            
            vals = adj_matrix[key]
            if len(vals)>0:
                for i in vals:
                    queue.append([key,i])
        
        max_val = 0
        while queue:
            buy_sell = queue.pop()
            sell_next = buy_sell[-1] +1
            val = adj_matrix.get(sell_next,[])
            while len(val)==0 and sell_next<len(prices):
                sell_next+=1
                val = adj_matrix.get(sell_next,[])
            if(len(val)>0):
                for i in adj_matrix[sell_next]:
                    new_sell = buy_sell[:]
                    new_sell.append(sell_next)
                    new_sell.append(i)
                    queue.append(new_sell)
            else:
                curr_val = 0 
                while buy_sell:
                    val1 = buy_sell.pop(0)
                    val2 = buy_sell.pop(0)
                    curr_val+= (prices[val2]-prices[val1])
                max_val = max(max_val,curr_val)
                
        return max_val
                    
if __name__ == "__main__":
    inp = [2,1,2,1,0,1,2]
    print(Solution().maxProfit(inp))
    inp = [3,2,6,5,0,3]
    print(Solution().maxProfit(inp))
    inp = [7,1,5,3,6,4]
    print(Solution().maxProfit(inp))
    inp = [1,2,3,4,5]
    print(Solution().maxProfit(inp))
    inp = [7,6,4,3,1]
    print(Solution().maxProfit(inp))
            
                    
        