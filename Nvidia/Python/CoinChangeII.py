"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

class Solution:
    def __init__(self):
        self.count = 0 
        self.visited = []
    def change(self, amount, coins):
        
        count = 0 
        def change_helper(comb):
            
            if(amount==sum(comb)):
                if(sorted(comb) not in self.visited):
                    self.count+=1
                    self.visited.append(sorted(comb))
            elif(sum(comb)>amount):
                return 0 
            else:
                # count = 0 
                for i in coins:
                    change_helper((*comb,i))
        change_helper(())
        return self.count


if __name__ == "__main__":
    amount = 5
    coins = [1,2,5]
    print(Solution().change(amount,coins))