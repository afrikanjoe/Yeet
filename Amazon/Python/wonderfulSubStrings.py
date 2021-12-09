"""
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), 
return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

"""


from collections import Counter
class Solution:
    def wonderfulSubstrings(self, word):
        counter = 0 
        for i in range(1,len(word)+1):
            for j in range(0,len(word)-i+1):
                if(self.is_wonderful(word[j:j+i])):
                    counter+=1
        return counter
                
                
    def is_wonderful(self,s):
        odd_count = 0 
        c = Counter(s)
        for val in c.values():
            if(val%2==1):
                odd_count+=1
            if(odd_count>1):
                return False
        return True

if __name__ == "__main__":
    word = "aabb"
    print(Solution().wonderfulSubstrings(word))

        
