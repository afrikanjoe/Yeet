"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""





from functools import lru_cache


class Solution:
    def coinChange(self, coins, amount):
        
        @lru_cache(maxsize=None)
        def coinChangeHelper(coins,amount,count):
            if(amount==0):
                return count
            else:
                ways = []
                for i in coins: 
                    if(amount-i>=0):
                        val = coinChangeHelper(coins,amount-i,count+1)
                        if(val>0):
                            ways.append(val)
                if(ways):
                    return min(ways)
                else:
                    return -1
        
        return coinChangeHelper(tuple(coins),amount,0)
        
if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    print(Solution().coinChange(coins,amount))