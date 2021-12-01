"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

class Solution:
    def letterCombinations(self, digits):
        if(not digits):
            return []
        letter_dict = {}
        a = ord('a')
        for i in range(2,10):
            if(i == 7 or i==9):
                counter =4 
            else:
                counter = 3
            for j in range(counter):
                val = letter_dict.get(i,[])
                val.append(chr(a))
                letter_dict[i] = val
                a+=1
        
        
        res = []
        queue = [digits]
        while queue:
            done = True
            val = queue.pop()
            for i in val:
                if(i.isnumeric()):
                    done=False
                    neighs = letter_dict[int(i)]
                    for j in neighs:
                        new_str = val.replace(i,j,1)
                        queue.append(new_str)
            if(done):
                if(val not in res):
                    res.append(val)
        return res
                        

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))