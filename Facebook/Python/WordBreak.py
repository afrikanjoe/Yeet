"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
"""




class Solution:
    def wordBreak(self, s, wordDict):
        
        res = []
        queue = [(s,[])]
        visited = []
        
        terminate_cond = len(s)*" "
        
        while queue:
            
            curr_word,curr_list = queue.pop(0)
            if(curr_word==terminate_cond):
                
                vals = sorted(curr_list)
                new_word = [i[1] for i in vals]
                if(new_word not in visited):
                    res.append(" ".join(new_word))
                    visited.append(new_word)
              
                  
            for word in wordDict:
                if(word in curr_word):
                    replace_str = len(word)*" "
                    index = curr_word.index(word)
                    new_str = curr_word.replace(word,replace_str,1)
                    new_list = curr_list[:] + [(index,word)]
                    queue.append((new_str,new_list))
        return res


if __name__ == "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    print(Solution().wordBreak(s,wordDict))