"""

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if 
the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

"""

class Solution:
    def combinationSum(self, candidates, target):
        
        
        queue =[[i] for i in candidates]
        ans = []
        
        while queue:
            
            curr_list =queue.pop()
            if(sum(curr_list)==target):
                if(sorted(curr_list) not in ans):
                    ans.append(sorted(curr_list))
            else:
                
                curr_sum = sum(curr_list)
                for i in candidates:
                    
                    if(curr_sum+i<=target):
                        new_list = curr_list[:]+[i]
                        queue.append(new_list)
        return ans


if __name__ == "__main__":
    cands = [2,3,5]
    target = 8
    print(Solution().combinationSum(cands,target))