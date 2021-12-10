"""We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string. For example, if s = "110001111000000", then groups = [2, 3, 4, 6].

For every binary string of the form '0' * k + '1' * k or '1' * k + '0' * k, the middle of this string must occur between two groups.

Let's try to count the number of valid binary strings between groups[i] and groups[i+1]. If we have groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000". We clearly can make min(groups[i], groups[i+1]) valid binary strings within this string. Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.

Algorithm

Let's create groups as defined above. The first element of s belongs in it's own group. From then on, each element either doesn't match the previous element, so that it starts a new group of size 1; or it does match, so that the size of the most recent group increases by 1.

Afterwards, we will take the sum of min(groups[i-1], groups[i]).
"""

from collections import Counter
class Solution:


    def countBinarySubstrings(self, s: str) -> int:
        
        
        groups = self.count_consec(s)
        
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
        
    def count_consec(self,s):
        curr_count = 0
        groups = []
        prev = s[0]
        for i in s:
            if(i==prev):
                curr_count+=1
            else:
                groups.append(curr_count)
                curr_count=1
                prev = i 
        groups.append(curr_count)
        return groups


    def countBinarySubstringsMyUninformedAttempt(self, s):
        
        
        count_dict = {}
        
        for i in range(1,self.count_consec2(s)):
            for j in range(2,len(s)+1):
                for k in range(0,len(s)-j+1):
                    
                    curr_str = s[k:k+j]
                    #consec = self.count_consec(curr_str)
                    c = Counter(curr_str)
                    if(c.get('1',0)==i):
                        tup = (i,c.get('0',0),c.get('1',0))
                        val = count_dict.get(tup,[])
                        val.append(curr_str)
                        count_dict[tup] = val
                    
        
    def count_consec2(self,s):
        ones_count = 0  
        curr_count = 0
        for i in s:
            if(i=="1"):
                curr_count+=1
                ones_count = max(curr_count,curr_count)
            else:
                curr_count=0 
        return ones_count 

if __name__ == "__main__":
    inp = "001100111"
    print(Solution().countBinarySubstrings(inp))