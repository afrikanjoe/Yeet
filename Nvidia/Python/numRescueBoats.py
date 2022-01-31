"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
"""

class Solution:
    def numRescueBoats(self, people,limit):
        
        boats = []
        people = sorted(people)[::-1]
        while people:
            
            person  = people[0]
            added = False
            for boat in boats:
                if(len(boat)<2 and boat[0]+person<=limit):
                    boat.append(person)
                    added = True
                    break
            if(not added):
                boats.append([person])
            people.pop(0)
        print(boats)
        return len(boats)

class OptimalSolution:
    def numRescueBoats(self, people, limit):
        
        boats = []
        people = sorted(people)
        high = len(people)-1
        low = 0
        boats = 0
        
        while low<=high:
            if(people[low]+people[high]<=limit):
                low+=1
                high-=1
            else:
                high-=1
            boats+=1
        return boats

if __name__ == "__main__":
    people = [5,1,7,4,2,4]
    limit = 7
    print(OptimalSolution().numRescueBoats(people,limit))
