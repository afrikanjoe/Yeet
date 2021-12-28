"""

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""


class Solution:
    def removeDuplicates(self, s, k):
        
        queue = [s]
        while queue:
            curr_str = queue.pop()
            new_str = None
            for i in range(len(curr_str)-k+1):
                
                curr_entr = curr_str[i:i+k]
                
                if(len(set(curr_entr))==1):        
                    new_str = curr_str[0:i] + curr_str[i+k:]
                    queue.append(new_str)
                    break
            if(new_str==None):
                break
        return curr_str


class OptimalSolution:
    def removeDuplicates(self, s, k):
        
        stack = []
        
        i= 0 
        while i<len(s):
            if(i==0 or s[i]!=s[i-1]):
                stack.append(1)
            else:
                stack[-1]+=1
                if(stack[-1]==k):
                    s = s[:i-k+1] + s[i+1:]
                    stack.pop()
                    i = i-k
            #increment counter
            i+=1
        return s

if __name__ == "__main__":
    s = "pbbcggttciiippooaais"
    k = 2
    print(Solution().removeDuplicates(s,k))
    s = "deeedbbcccbdaa"
    k = 3
    print(Solution().removeDuplicates(s,k))
        