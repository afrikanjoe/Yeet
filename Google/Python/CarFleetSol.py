"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""

class Solution:
    def carFleet(self, target, position, speed):
        times =[]
        speed_dict = {}
        fleets = 0
        # create a dictionary with the car's position and value
        # sort the list so we can go from back to front.
        for i in range(len(position)):
            speed_dict[position[i]] = speed[i]
        sorted_positions = sorted(position)
        print(sorted_positions)
        
        for i in range(len(sorted_positions)):
            times.append((target - sorted_positions[i])/speed_dict[sorted_positions[i]])
        
        print(times)
        while times:
            # get time of last car in stack
            time = times.pop()
            print("cur",time)
            # if there is a car behind current car
            # that would take less or equal time to finish, then combine fleet
            while times and times[-1] <= time:
                print("same",times[-1])
                times.pop()
            fleets += 1
        return fleets





if __name__ == "__main__":
    # Answer = 3
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(Solution().carFleet(target,position,speed))
    # # Answer = 2
    # target = 10
    # position=[6,8]
    # speed=[3,2]
    # print(Solution().carFleet(target,position,speed))
    # # Answer = 1
    # target = 10
    # position=[2,4]
    # speed =[3,2]
    # print(Solution().carFleet(target,position,speed))
    # # Answer = 2
    # target =10
    # position = [0,2]
    # speed = [1,1]
    # print(Solution().carFleet(target,position,speed))