"""

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: 
each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

"""

class Solution:
    def count_differences(self,file):
        arr = file.split("\n")
        count = 0 
        for i in range(len(arr)-1):
            if(int(arr[i])<int(arr[i+1])):
                count+=1
        return count 

    def count_differences_part_two(self,file):
        arr = file.split("\n")
        count = 0 
        prev = int(arr[0])+int(arr[1])+int(arr[2])
        for i in range(1,len(arr)-2):
            curr_sum = int(arr[i])+int(arr[i+1])+int(arr[i+2])
            if(curr_sum>prev):
                count+=1
            prev = curr_sum 
        return count 



if __name__ == "__main__":
    with open("inputs/Day1.txt") as f:
        content = f.read()
        print(Solution().count_differences(content))

    with open("inputs/Day1.txt") as f:
        content = f.read()
        print(Solution().count_differences_part_two(content))