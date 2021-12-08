"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""

class Solution:
    def groupAnagrams(self, strs):
        
        anagram_dict = {}
        
        
        letter_count = {}
        for i in range(0,26):
            letter_count[i] = 0
            
            
        for st in strs:
            curr_count = dict(letter_count)
            for letter in st:
                curr_count[ord(letter)-97]= curr_count.get(ord(letter)-97,0)+1
            
            val = anagram_dict.get(tuple(curr_count.values()),[])
            val.append(st)
            anagram_dict[tuple(curr_count.values())] = val
        return list(anagram_dict.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))
