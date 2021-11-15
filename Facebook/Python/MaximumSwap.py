"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
"""

class Solution:
    def maximumSwap(self, num):
        
        num_list= list(str(num))
        left_most_min = 1e9
        left_most_min_index = len(num_list)-1
        right_most_max = -1e9
        right_most_max_index = len(num_list)-1
        
        for i in range(len(num_list)-1,-1,-1):
            curr_val = int(num_list[i])
            if(curr_val>right_most_max):
                right_most_max = curr_val
                right_most_max_index = i 
            elif(curr_val<right_most_max):
                left_most_min = curr_val
                left_most_min_index = i
                              
        if(left_most_min_index<right_most_max_index):
            self.swap(num_list,left_most_min_index,right_most_max_index)
        else:
            while (right_most_max_index < len(num_list)-1):
                right_most_max = -1e9
                for i in range(len(num_list)-1,right_most_max_index,-1):
                    curr_val = int(num_list[i])
                    if(curr_val>right_most_max):
                        right_most_max = curr_val
                        right_most_max_index = i 
                    elif(curr_val<right_most_max):
                        left_most_min = curr_val
                        left_most_min_index = i
                if(left_most_min_index<right_most_max_index):
                    self.swap(num_list,left_most_min_index,right_most_max_index)
                    return int("".join(num_list))
        return int("".join(num_list))
    
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    nums = 19931105
    print(Solution().maximumSwap(nums))