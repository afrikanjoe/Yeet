import heapq 

"""
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory.
For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, 
so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).
You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. 
You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.
Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

"""

class Solution:
    def maxProfit(self, inventory, orders):
        
        heap  = []
        for i in inventory:
            heapq.heappush(heap,-i)
        ans = 0 
        for i in range(orders):
            new_val = heapq.heappop(heap)
            new_val = -new_val
            ans+= new_val
            if(new_val-1>0):
                heapq.heappush(heap,-(new_val-1))
        
        mod = (10**9)+7
        return ans%mod

    import heapq 

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse = True)        
        i=colors=1
        cur_value=inventory[0]
        profit=0
        while orders>0:
            while i<len(inventory) and inventory[i]==cur_value:
                colors+=1
                i+=1
            if orders<colors:
                profit+=orders*cur_value
                break
            next_value = 0 if i>=len(inventory) else inventory[i]
            steps = min(orders, (cur_value-next_value)*colors)//colors
            profit+=colors*steps*(cur_value+cur_value-steps+1)//2
            orders-=steps*colors
            cur_value-=steps
        return profit%(10**9 + 7)

if __name__ == "__main__":
    inventory = [2,8,4,10,6]
    orders = 20
    print(Solution().maxProfit(inventory,orders))