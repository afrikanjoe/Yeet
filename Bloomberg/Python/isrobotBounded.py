"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
"""



class Solution:
    def isRobotBounded(self, instructions):
        
        
        direction = 0 
        x= 0 
        y = 0 
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        for i in range(len(instructions)):
            if(instructions[i]=="G"):
                x = x+ directions[direction][0]
                y = y+ directions[direction][1]
            elif(instructions[i]=="L"):
                direction=(direction+1)%4
            else:
                direction=(direction+3)%4
                
                
        
        return ((x,y)==(0,0) or direction!=0)

if __name__ == "__main__":
    instructions = "GGLLGG"
    print(Solution().isRobotBounded(instructions))