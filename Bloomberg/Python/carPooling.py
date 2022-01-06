"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates 
that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. 
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

"""

class Solution:
    def carPooling(self, trips, capacity):

        start_times = {}
        end_times = {}
        
        for i in trips:
            
            start_times[i[1]] = start_times.get(i[1],0)+ i[0]
            end_times[i[2]] = end_times.get(i[2],0)+ i[0]
            
        
        capacity_left = capacity
        index = 0
        while index<=1000 and capacity_left>=0:
            capacity_left +=  end_times.get(index,0)
            capacity_left -=  start_times.get(index,0)
            index+=1
            
        return capacity_left>=0


if __name__ == "__main__":
    trips = [[9,0,1],[3,3,7]]
    capacity = 4
    print(Solution().carPooling(trips,capacity))
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    print(Solution().carPooling(trips,capacity))