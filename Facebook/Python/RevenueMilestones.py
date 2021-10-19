"""
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. 
Given an array of the revenue on each day,  and an array of milestones Facebook wants to reach, 
return an array containing the days on which Facebook reached every milestone.
"""

def getMilestoneDays(revenues, milestones):
  # Write your code here
  ms = []
  for i in range(len(milestones)):
    ms.append((milestones[i],i))
  ms = sorted(ms)

  rev_sum = 0 
  outp = []
  for i in range(1,len(revenues)+1):
    rev_sum += revenues[i-1]
    while ms:
      milestone = ms[0]
      if(rev_sum>=milestone[0]):
        outp.append((milestone[1],i))
        ms.pop(0)
      else:
        break
  outp = sorted(outp)
  
  return [i[1] for i in outp]