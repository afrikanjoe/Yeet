"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
"""

class Solution:
    def partition(self, s):
        
        queue = [(s,[])]
        
        tups = []
        
        while queue:
            s_new, partition  = queue.pop()
            if(not s_new):
                
                add = True
                for i in partition:
                    if(i!=i[::-1]):
                        add = False
                if(add):
                    tups.append(partition)
            else:
                for i in range(len(s_new)):
                    new_list = partition[:]
                    
                    curr_s=s_new[:i+1]
                    curr_left=s_new[i+1:]
                    
                    new_list = new_list + [curr_s]
                    new_tup = (curr_left,new_list)
                    queue.append(new_tup)
        return tups

if __name__ == "__main__":
    s="aaabb"
    print(Solution().partition(s))
