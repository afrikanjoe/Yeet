"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
"""

class Solution:
    def shipWithinDays(self, weights, days):
        
        low = max(weights)
        high = sum(weights)
        
        while low<high:
            
            mid = (low + high)>>1
            if(self.canShip(mid,weights,days)):
                high = mid
            else:
                low = mid+1
        return high
            
    
    def canShip(self,capacity,weights,days):
        day_count = 0 
        weight = 0 
        for i in weights:
            weight+= i
            if(weight>capacity):
                day_count+=1
                weight=i
        return day_count<days


if __name__ == "__main__":
    weights = [3,2,2,4,1,4]
    days = 3
    print(Solution().shipWithinDays(weights,days))