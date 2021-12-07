import numpy as np
class Solution:
    def compute_optimal_position(self,inp_arr):
        arr = np.asarray(inp_arr)
        fuels = [2**32]
        for i in range(1,len(inp_arr)):

            diff = np.abs(arr - i).sum()
            print(diff)
            fuels.append(diff) 
        
        min_day = min(fuels)
        print("Min Fuel,",min_day)
        return fuels.index(min_day)

    def compute_optimal_position_part_two(self,inp_arr):
        arr = inp_arr
        fuels = [2**32]
        for i in range(1,len(inp_arr)):
            
            
            f_spent = [self.fuel_sum(j-i) for j in arr]
            fuels.append(sum(f_spent))
            #print(f_spent,sum(f_spent))
        
        min_day = min(fuels)
        print("Min Fuel,",min_day)
        return fuels.index(min_day)


    def fuel_sum(self,val):
        val = abs(val)
        return int((val*(val+1))/2)

with open("inputs/Day7.txt") as f:
        line = f.readline().replace("\n","").split(",")
        line = [int(i) for i in line]
        print(Solution().compute_optimal_position(line))
        print("Part Two:")
        print(Solution().compute_optimal_position_part_two(line))