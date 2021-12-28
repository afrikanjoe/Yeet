"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. 
For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. 
If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

"""

class Solution:
    def groupThePeople(self, groupSizes):
        
        
        self.groups = {}
        
        for i in range(len(groupSizes)):
            
            val = self.groups.get(groupSizes[i],[])
            val.append(i)
            self.groups[groupSizes[i]] = val
            
        
        # return groups 
        ans = []
        for key in self.groups:
            
            grouping = []
            for index in self.groups[key]:
                
                if len(grouping)<key:
                    grouping.append(index)
                else:
                    ans.append(grouping)
                    grouping = [index]
            if(grouping):
                ans.append(grouping)
        return ans

if __name__ == "__main__":
    groupSizes = [3,3,3,3,3,1,3]
    print(Solution().groupThePeople( groupSizes))
    groupSizes = [2,1,3,3,3,2]
    print(Solution().groupThePeople( groupSizes))
