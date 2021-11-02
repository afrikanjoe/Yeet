"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example: 
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s):
        index1 = 0
        index2 = len(s)-1
        while index1<index2:
            val1 = s[index1] 
            val2 = s[index2]
            if(not val1.isalpha() and not val1.isnumeric()):
                index1+=1
                continue
            if(not val2.isalpha() and not val2.isnumeric()):
                index2-=1
                continue
            if(s[index1].lower()!=s[index2].lower()):
                return False
            index1+=1
            index2-=1
        return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))