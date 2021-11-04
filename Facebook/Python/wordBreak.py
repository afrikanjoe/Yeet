"""

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

class Solution:
    def wordBreak(self, s, wordDict):
        queue = [s]
        visited = []
        valid = len(s)*" "
        while queue:
            curr_word = queue.pop()
            for word in wordDict:
                new_word = str(curr_word)
                new_word = new_word.replace(word," "*len(word),1)
                if(new_word==valid):
                    return True
                else:
                    if new_word not in visited:
                        visited.append(new_word)
                        queue.append(new_word)
        return False
        


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    print(Solution().wordBreak(s,wordDict))
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(Solution().wordBreak(s,wordDict))