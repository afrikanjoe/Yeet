"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution:
    def maxProfitBF(self, prices):
        
        profit = 0 
        for i in range(len(prices)-1):
            
            num = prices[i]
            profit = max(profit, max(prices[i+1:])- num)
        return profit 

    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0 
        for i in range(len(prices)):
            num = prices[i]
            profit = max(profit, num-min_price)
            if(num<min_price):
                min_price = num
        return profit 

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))