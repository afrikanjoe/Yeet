"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

"""

class Solution:
    def combinationSum2(self, candidates, target):
        
        queue = [[[(c,i)],c] for i,c in enumerate(candidates)]
        ans = []
        while queue:
            
            comb,curr_sum = queue.pop(0)
            if(curr_sum==target):
                comb = sorted([i[0] for i in comb])
                if(comb not in ans):
                    ans.append(comb)
            for i,c in enumerate(candidates):
                
                if((c,i) in comb):
                    continue
                else:
                    if(curr_sum+c<=target):
                        new_list = comb[:] +[(c,i)]
                        new_sum = curr_sum+c
                        queue.append([new_list,new_sum])
        return ans
            
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(Solution().combinationSum2(candidates,target))