"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. 

For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

"""

from collections import Counter

class Solution:
    def minDeletionsBF(self, s):
        
        orig_len = len(s)
        queue = [s]
        num_dels = 2*32 
        visited = []
        while queue:
            curr_str = queue.pop(0)
            visited.append(curr_str)
            if(self.is_good(curr_str)):
                curr_dels = orig_len - len(curr_str)
                num_dels  = min(num_dels,curr_dels)
                break
            else:
                for i in range(len(curr_str)):
                    new_str = curr_str[0:i] + curr_str[i+1:]
                    if(new_str not in visited):
                        queue.append(new_str)
        return num_dels
        
        
    def is_good(self,s):
        
        c = Counter(s).values()
        if(len(set(c))==len(c)):
            return True
        else:
            return False

import heapq


class OptimalSolution:
    def minDeletions(self, s):
        heap = []
        c = Counter(s)
        for key in c.keys():
            heapq.heappush(heap,(-c[key],key))
            
        count = 0 
        prevs = []
        while heap:
            
            tup = heapq.heappop(heap)
            val = - tup[0]
            if(len(prevs)==0):
                prevs.append(val)
            elif(prevs[-1]<=1):
                count+=val
            elif(prevs[-1]<=val):
                while(val>=prevs[-1]):
                    val = val-1
                    count+=1
                prevs.append(val)
            else:
                prevs.append(val)
        return count


if __name__ == "__main__":
    s = "abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz"
    print(OptimalSolution().minDeletions(s))