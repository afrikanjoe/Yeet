def maxProfitBruteForce(self, prices):
    keys = [(i,j) for i in range(len(prices)) for j in range(len(prices)) if i!=j and j>i]
    profit = 0 
    for key in keys:
        prof = (prices[key[1]]-prices[key[0]])
        if (prof>profit):
            profit =prof
    return profit

def maxProfit(prices):
        currProfit, maxProfit = 0,0        
        for i in range(1, len(prices)):
            currTick = prices[i] - prices[i-1]
            currProfit = max(currTick, currTick + currProfit)
            maxProfit = max(currProfit, maxProfit)
        return maxProfit