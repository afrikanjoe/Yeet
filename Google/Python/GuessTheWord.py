"""

This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.


"""





class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        wordSet = list(set(wordlist))
        guesses = 0
        
        while wordSet and guesses < 10:
            cur = wordSet.pop()
            matchCount = master.guess(cur)
            wordSet = [x for x in wordSet if matchCount ==self.match_word(cur, x)]
            guesses+=1
            
            
    def match_word(self,word1,word2):
        match_count = 0
        if(len(word1)<6 or len(word2)<6):
            return 0
        for i in range(len(word1)):
            if(word1[i]==word2[i]):
                match_count+=1
        return match_count
        