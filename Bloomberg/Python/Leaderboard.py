class Leaderboard:

    def __init__(self):
        self.dict = {}

    def addScore(self, playerId: int, score: int):
        
        val = self.dict.get(playerId,0)+score
        self.dict[playerId]=val
        

    def top(self, K: int) -> int:
        values = sorted(list(self.dict.values()),reverse=True)
        return sum(values[:K])

    def reset(self, playerId: int):
        self.dict[playerId] = 0 
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)