class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combs = []
        
        queue = [[i] for i in range(1,n+1)]
        while queue:
            
            comb = queue.pop(0)
            if(len(comb)==k):
                if(sorted(comb) not in combs):
                    combs.append(sorted(comb))
            else:
                for i in range(1,n+1):
                    new_comb = comb[:]
                    if(i not in new_comb):
                        new_comb.append(i)
                        queue.append(new_comb)
        return combs