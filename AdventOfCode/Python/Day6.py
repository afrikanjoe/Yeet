
import numpy as np
class Solution:

    def simulate_laternfish(self,inp):
        count = 0 
        nums = inp[:]
        while count< 256:
            new_fish = []
            for i in range(len(nums)):

                if(nums[i]>0):
                    nums[i]-=1
                else:
                    new_fish.append(8)
                    nums[i]=6
            nums = nums + new_fish
            count+=1
        print(len(nums))

    
    def numpy_implementation(self,inp):
        count = 0 
        nums = np.asarray(inp)
        while count< 256:
            new_fish = []


            # part1
            
            zero_indices = np.where(nums==0)[0] 
            if(len(zero_indices)>0):
                new_fish = np.asarray([9]*len(zero_indices))
                nums[zero_indices] = 7 
                nums = np.hstack([nums,new_fish])

            # part 2
            indices = np.where(nums>0)[0]
            nums[indices]-=1
            
            
            count+=1
        
        print(len(nums))


    





if __name__ == "__main__":
    inp = [3,4,3,1,2]
    Solution(). numpy_implementation(inp)
    with open("inputs/Day6.txt") as f:
        line = f.readline().replace("\n","").split(",")
        line = [int(i) for i in line]
        Solution().simulate_laternfish(line)