"""
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. 
locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

"""
class Solution:
    def canBeValid(self, s, locked):
        
        locked_open = []
        unlocked = []
        
        for i, c in enumerate(s):
            if locked[i] == '0':
                unlocked.append(i)
            else:
                # if the bracket is locked an open add it to locked open
                if c == '(':
                    locked_open.append(i)
                # otherwise if it's locked and closed then try and pop from 
                # the locked open or unlocked closed 
                # if we can't then we can't proceed
                else:
                    if locked_open:
                        locked_open.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False
        # if we have locked open brackets 
        # then we need unlocked characters after this bracekt
        while locked_open:
            if unlocked and unlocked[-1] > locked_open[-1]:
                unlocked.pop()
                locked_open.pop()
            else:
                return False
        return len(unlocked)%2 ==0 
        
if __name__ == "__main__":
    s = "())()))()(()(((())(()()))))((((()())(())"
    l= "1011101100010001001011000000110010100101"
    print(Solution().canBeValid(s,l))
    
    
  