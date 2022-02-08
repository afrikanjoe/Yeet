"""
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num):
        
        val = list(str(num))
        while len(val)>1:
            
            curr_sum = 0 
            for i in val:
                curr_sum+=int(i)
            val = list(str(curr_sum))

        return int(val[0])

if __name__ == "__main__":
    num = 138
    print(Solution().addDigits(num))