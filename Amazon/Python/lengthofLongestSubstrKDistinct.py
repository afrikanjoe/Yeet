"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
"""




from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def lengthOfLongestSubstringKDistinctBF(self, s, k):
        if(not s):
            return 0
        elif(len(set(s))<=k):
            return len(s)
        else:
            return max(self.lengthOfLongestSubstringKDistinct(s[1:],k),self.lengthOfLongestSubstringKDistinct(s[:-1],k))

    # Sliding Window Approach
    def lengthOfLongestSubstringKDistinctSlide(self, s: str, k: int) -> int:
        
        max_len = 0 
        for i in range(1,len(s)+1):
            added = False
            for j in range(0,len(s)-i+1):
                
                if(len(set(s[j:j+i]))<=k):
                    s_len = len(s[j:j+i])
                    if(s_len>max_len):
                        max_len = s_len
                        added = True
            if(not added):
                break
        return max_len


     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if(k==0):
            return 0 
        
        left  = 0 
        right = 0
        
        max_len = 1
        char_dict = {}
        
        while right < len(s):
            
            # move the pointer to the right
            char_dict[s[right]] = right
            right+=1
            
            # if we have added to many characters, delete the left_most character
            if(len(char_dict.keys())==k+1):
            
                # this is genius
                del_idx  = min(char_dict.values())
                del char_dict[s[del_idx]]
                
                # move left right
                left = del_idx + 1
                
            max_len = max(max_len,right-left)
            
        return max_len
            

if __name__ == "__main__":
    s = "aaabbccdd"
    k = 2
    print(Solution().lengthOfLongestSubstringKDistinct(s,k))
            
            
        