"""

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

"""

class Solution:
    def divisorGame(self, n):
        AliceWins = False
        while n >=2:
            n = n-1 
            AliceWins = not AliceWins
        return AliceWins



        

if __name__ == "__main__":
    n= 2 
    print(Solution().divisorGame(n))

    n = 3 
    print(Solution().divisorGame(n))

    n = 1 
    print(Solution().divisorGame(n))