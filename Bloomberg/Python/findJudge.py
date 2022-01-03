"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

"""

class Solution:
    def findJudge(self, n, trust):
        
        trusts = {i:0 for i in range(1,n+1)}
        
        trusted = {i:0 for i in range(1,n+1)}
        
        for tup in trust:
            
            trusts[tup[0]] = trusts[tup[0]]+1
            trusted[tup[1]] = trusted[tup[1]]+1
            
        
        for key in trusts.keys():
            
            if(trusts[key]==0 and trusted[key]==n-1):
                return key
        return -1

if __name__ == "__main__":
    n = 2
    trust = [[1,2]]
    print(Solution().findJudge(n,trust))

    n = 3
    trust = [[1,3],[2,3]]
    print(Solution().findJudge(n,trust))

    n = 3
    trust = [[1,3],[2,3],[3,1]]
    print(Solution().findJudge(n,trust))