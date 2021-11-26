class Solution:
    def findCelebrityBF(self, n):
        
        know_dict = {}
        visited =[]
        knowns = []
        for i in range(n):
            for j in range(n):
                if(i==j or (i,j) in visited):
                    continue
                else:
                    
                    ab = knows(i,j)
                    if(ab):
                        val = know_dict.get(j,[])
                        val.append(i)
                        if(i not in knowns):
                            knowns.append(i)
                        know_dict[j] = val
                    ba = knows(j,i)
                    if(ba):
                        val = know_dict.get(i,[])
                        val.append(j)
                        if(j not in knowns):
                            knowns.append(j)
                        know_dict[i] = val
                    visited.append((i,j))
                    visited.append((j,i))
        for key in know_dict.keys():
            fans = know_dict[key]
            if(len(fans)==n-1 and key not in knowns):
                return key
        return -1

     def findCelebrityOptimal(self, n):
        
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            if knows(i, j) or not knows(j, i):
                return False
        return True