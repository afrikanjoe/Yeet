"""
You are given an array representing a row of seats where seats[i] = 1 
represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Example: 
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
"""


"""
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. 
Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

"""


""""""

class Solution:
    def rotatedDigits(self, n):
        replace_dict = {2:5,5:2,6:9,9:6,0:0,1:1,8:8}
        
        keys = list(replace_dict.keys())
            
        count= 0 
        for i in range(1,n+1):
            num = str(i)
            num2 = ""
            valid = True
            for j in num:
                
                if int(j) not in keys:
                    valid = False
                    break
                
                num2 = num2+str(replace_dict[int(j)])
            if(num2!=num and valid):
                count+=1
        return count

    def maxDistToClosest(self, seats):
        
        # left pass
        previous_occupied = None
        dist = []
        for i in range(len(seats)):
            if(seats[i]):
                previous_occupied = i
                dist.append(-1e9)
                continue
            if (previous_occupied==None and not seats[i]):
                dist.append(1e9)
            else:
                dist.append(abs(i-previous_occupied))
        
        # right pass
        for i in range(len(seats)-1,-1,-1):
            if(seats[i]):
                previous_occupied = i
                continue
            else:
                dist[i]=min(abs(i-previous_occupied),dist[i])
        return max(dist)


if __name__ == "__main__":
    n = 857 
    print(Solution().rotatedDigits(n))

    seats = [1,0,0,0,1,0,1]
    print(Solution().rotatedDigits(seats))