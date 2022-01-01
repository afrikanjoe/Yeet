"""The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. 
You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]


"""

class Solution:
    def findRepeatedDnaSequences(self, s):
        
        dicta = {}
        
        for i in range(len(s)-10+1):
            dicta[s[i:i+10]] = dicta.get(s[i:i+10],0)+1
        
        ans = []
        for key in dicta.keys():
            if(dicta[key]>1):
                ans.append(key)
        return ans

if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))