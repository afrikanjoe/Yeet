"""
There are n projects numbered from 0 to n - 1. You are given an integer array milestones where each milestones[i] 
denotes the number of milestones the ith project has.

You can work on the projects following these two rules:

Every week, you will finish exactly one milestone of one project. You must work every week.
You cannot work on two milestones from the same project for two consecutive weeks.
Once all the milestones of all the projects are finished, or if the only milestones that you can work on 
will cause you to violate the above rules, you will stop working. Note that you may not be able to finish 
every project's milestones due to these constraints.

Return the maximum number of weeks you would be able to work on the projects without violating the rules mentioned above.

"""
class Solution:
    def numberOfWeeks(self, milestones):
        
        milestones = sorted(milestones,reverse=True)
        s = sum(milestones)
        others = s - milestones[0]
        # if the max project has a value less than the sum of all the other projects then we can finish
        
        if(milestones[0]<=others):
            return sum(milestones)
        else:
            return (2*others)+1

if __name__ == "__main__":
    ms = [1,2,3]
    print(Solution().numberOfWeeks(ms))
    ms = [100,2,3]
    print(Solution().numberOfWeeks(ms))
    ms = [9,5,4]
    print(Solution().numberOfWeeks(ms))