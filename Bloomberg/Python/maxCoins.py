"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 
goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167


"""

class Solution:
    def maxCoins(self,nums):
        
        
        queue = [(0,nums)]
        max_coins  = 0 
        while queue:
            
            curr_val,baloons = queue.pop()
            if(not baloons):
                max_coins = max(max_coins,curr_val)
            else:
                
                for i in range(len(baloons)):
                    
                    prev = i-1
                    after = i +1
                    
                    if(prev<0):
                        prev = 1
                    else:
                        prev = baloons[i-1]
                        
                    if(after>len(baloons)-1):
                        after = 1
                    else:
                        after = baloons[i+1]
                        
                    new_val = curr_val + (after*prev*baloons[i])
                    new_list  = baloons[0:i] +baloons[i+1:]
                    new_tup = (new_val,new_list)
                    queue.append(new_tup)
        return max_coins


# This still has O(N* 2^N) complexity
from functools import lru_cache
class BetterSolution:
    def maxCoins(self, nums):
        
        @lru_cache(maxsize=None)
        def helper(val,baloons):
            
            if(not baloons):
                return val 
            else:
                
                vals = []
                for i in range(len(baloons)):
                    if(i-1>=0):
                        prev = baloons[i-1]
                    else:
                        prev = 1
                    
                    if(i+1<len(baloons)):
                        after = baloons[i+1]
                    else:
                        after = 1
                    vals.append(prev*after*baloons[i]+helper(val,baloons[0:i]+baloons[i+1:]))
                return val + max(vals)
            
        return helper(0,tuple(nums))
                        
                    
if __name__ == "__main__":
    nums = [3,1,5,8]
    print(Solution().maxCoins(nums))

    nums = [7,9,8,0,7,1,3,5,5,2,3]
    print(BetterSolution().maxCoins(nums))

                    
                
                
            
            