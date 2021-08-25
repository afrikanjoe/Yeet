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
        num_fleets = 0
        speed_dict ={}
        multi_car_fleet = False
        
        if(len(position)==1):
            return 1
        # create a dictionary with the car's position and value
        # sort the list so we can go from back to front.
        for i in range(len(position)):
            speed_dict[position[i]] = speed[i]
        sorted_positions = sorted(position)

        for i in range(len(position)-1):
            # get the cars and their speed
            car1 = sorted_positions[i]
            car2 = sorted_positions[i+1]
           
            car1_speed = speed_dict[car1]
            car2_speed = speed_dict[car2]

            if(car2_speed>car1_speed):
                num_fleets+=1
            elif(car1_speed == car1_speed and car2>car1):
                num_fleets+=2
            else:
                car1_step = car1+car1_speed
                car2_step = car2+car2_speed
                multi_car_fleet = True
                if(car1_step==car2_step and car1_step==target):
                    num_fleets+=1
                    multi_car_fleet = False
                elif(car2_step>=target):
                    num_fleets+=2
                    multi_car_fleet = False

        
        if(multi_car_fleet):
            num_fleets+=1
        
        return num_fleets

if __name__ == "__main__":
    # Answer = 3
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(Solution().carFleet(target,position,speed))
    # Answer = 2
    target = 10
    position=[6,8]
    speed=[3,2]
    print(Solution().carFleet(target,position,speed))
    # Answer = 1
    target = 10
    position=[2,4]
    speed =[3,2]
    print(Solution().carFleet(target,position,speed))
    # Answer = 2
    target =10
    position = [0,2]
    speed = [1,1]
    print(Solution().carFleet(target,position,speed))