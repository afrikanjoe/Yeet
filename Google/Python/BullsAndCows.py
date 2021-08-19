"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.


Input: secret = "1807", guess = "7810"
Output: "1A3B"

Input: secret = "1123", guess = "0111"
Output: "1A1B"

Input: secret = "1", guess = "0"
Output: "0A0B"
"""


class Solution:
    def getHint(self, secret, guess):
        str_ans = "{}A{}B"
        bulls = 0
        cows = 0
        seen = {}
        seen2 = {}
        for i in range(len(secret)):
            if(secret[i]==guess[i]):
                bulls+=1
            else:
                seen[secret[i]] = seen.get(secret[i],0)+1
                seen2[guess[i]] = seen2.get(guess[i],0)+1
                if(seen2.get(secret[i])):
                    cows+=1
                    seen2[secret[i]]=seen2[secret[i]]-1
                    seen[secret[i]]=seen[secret[i]]-1
                if(seen.get(guess[i])):
                    cows+=1
                    seen[guess[i]] =seen[guess[i]]-1
                    seen2[guess[i]]= seen2[guess[i]]-1
        return str_ans.format(bulls,cows)
                

if __name__=="__main__":
    secret = "1807"
    guess = "7810"
    print(Solution().getHint(secret,guess))
    secret = "1234"
    guess= "0111"
    print(Solution().getHint(secret,guess))
    secret="1122"
    guess="2211"
    print(Solution().getHint(secret,guess))
    secret="2962"
    guess="7236"
    print(Solution().getHint(secret,guess))
