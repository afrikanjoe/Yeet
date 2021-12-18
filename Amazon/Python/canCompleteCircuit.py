"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the 
circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

"""

class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        n = len(gas)
        for i in range(len(gas)):
            
            index = i 
            count = 0 
            gas_left = gas[i]
            while gas_left>=0 and count<n:
                gas_left = gas_left - cost[(index)%n] 
                if(gas_left<0):
                    break
                gas_left+= gas[(index+1)%n]
                count+=1
                index+=1
            if(count==len(gas) and gas_left>0):
                return i
            
        return -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas,cost))