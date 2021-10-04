
"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


I didn't get this, but this is a perfect candidate for binary search. This is cool.
"""


class Solution:
    def minimumEatingSpeed(self,piles,h):
        low = 1
        high = max(piles)
        mid = (low+high) // 2
        min_k = high

        while low<= high:
            valid =self.possible_solution(piles,mid,h)
            if(valid):
                min_k = min(min_k,mid)
                high = mid -1 
            else:
                low = mid + 1

            mid =  (low+high) // 2
        return (min_k)







    def possible_solution(self,piles,k,h):
        eat = [self.ceiling_division(i,k) for i in piles]
        return sum(eat)<=h

    def ceiling_division(self,n, d):
        return (n + d - 1) // d

        


if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(Solution().minimumEatingSpeed(piles,h))

    piles = [30,11,23,4,20]
    h = 5
    print(Solution().minimumEatingSpeed(piles,h))

    piles = [30,11,23,4,20]
    h = 6
    print(Solution().minimumEatingSpeed(piles,h))