"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

"""


class Solution:
    def maxScoreSlow(self, cardPoints, k):
        
        # case where we have to take all the cards
        if(k>len(cardPoints)):
            return sum(cardPoints)
        
        max_score = 0
        # sliding window
        
        for i in range(len(cardPoints)-k,len(cardPoints)+1):
            curr = cardPoints[i:i+k]
            curr_sum = sum(curr)
            if((i+k)>len(cardPoints)):
                runover = (i+k)%len(cardPoints)
                #print(curr_sum,cardPoints[0:runover])
                curr_sum+=sum(cardPoints[0:runover])
            max_score = max(curr_sum,max_score)
        return max_score

    def maxScore(self, cardPoints, k):
            """
            :type cardPoints: List[int]
            :type k: int
            :rtype: int
            """

            ans = sum(cardPoints[:k])
            cur = ans

            for i in range(1, k+1):
                deduct = cardPoints[k-i]
                increm = cardPoints[-i]
                cur = cur + increm - deduct
                ans = max(ans, cur)
            return ans
    

if __name__ == "__main__":
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(Solution().maxScore(cardPoints,k))
    cardPoints = [2,2,2]
    # k = 2
    # print(Solution().maxScore(cardPoints,k))
    # cardPoints = [9,7,7,9,7,7,9]
    # k = 7
    # print(Solution().maxScore(cardPoints,k))
    # cardPoints = [1,1000,1]
    # k = 1
    # print(Solution().maxScore(cardPoints,k))
    # cardPoints = [1,79,80,1,1,1,200,1]
    # k = 3
    # print(Solution().maxScore(cardPoints,k))