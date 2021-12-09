"""
Given an integer denoting a total number of wheels, help Amazon Logistics find the number of different ways to choose a fleet of vehicles from an infinite supply of two-wheeled
and four-wheeled vehicles such that the group of chosen vehicles that has that exact total number of wheels. 
Two ways of choosing vehicles are considered to be different if and only if they 
contain different numbers of two-wheeled or four-wheeled vehicles 

For example if our array wheels [4,5,6] our return array would be res = [2,0,2]. Case by case, we can have 1 four-wheel or 2 two-wheel to have 4 wheels. We cannot have 5 wheels or 3 for that matter


"""

class Solution:

    def chooseFleets(self,wheels):
        
        # Write your code here 
        ans = []
        for i in wheels: 
            ans.append(self.compute_ways_better(i))
        return ans 

    def chooseFleetsBad(self,wheels):
        
        # Write your code here 
        ans = []
        for i in wheels: 
            ans.append(self.compute_ways_bad(i))
        return ans 

    def compute_ways_bad(self,n):

        if(n%2==1):
            return 0
        else:
            count = 0 
            visited = []
            queue = [(n,{2:0,4:0})]
            while queue: 
                fleet_combo = queue.pop()
                wheels_left , curr_comb = fleet_combo[0], fleet_combo[1]
                if(wheels_left==0):
                    if(curr_comb not in visited):
                        count+=1
                        visited.append(curr_comb)
                else:
                    for i in range(2,6,2):
                        if((wheels_left-i)>=0):
                            new_comb = dict(curr_comb)
                            new_comb[i]+=1
                            queue.append((wheels_left-i,new_comb))
            return count
    # from reading online it looks like its num / 4 + 1
    def compute_ways_better(self,n):

        if(n%2==1):
            return 0
        else:
            return int((n/4)+1)

if __name__ == "__main__":
    inp=[4,5,6,0,2,4,6,8,10,12,14,16,18]
    print(Solution().chooseFleets(inp))
    print(Solution().chooseFleetsBad(inp))


