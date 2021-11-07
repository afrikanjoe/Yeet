"""
Calculuate all the permutations of a string need to learn this 
After the last Google Interview
"""
import copy
class Solution:
    
    
    def __init__(self):
        self.results_dict = []
        
    def calculate_permutations(self,inp_str,i):
        append_str = "".join(inp_str)
        if(append_str not in self.results_dict):
            self.results_dict.append( append_str)
        if(i<len(inp_str)-1):
            for j in range(i+1,len(inp_str)):
                new_str = inp_str[:]
                self.swap(new_str,i,j)
                self.calculate_permutations(new_str,i+1)




        

    def calculate_all_permutations(self,inp_str):
        self.calculate_permutations(list(inp_str),-1)
        return self.results_dict

    def swap(self,arr,i,j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
            
            
        
        
if __name__ == "__main__":
    s = "ABC"
    print(sorted(Solution().calculate_all_permutations(s)))
    s = "BAC"
    print(sorted(Solution().calculate_all_permutations(s)))
    s = "ABCD"
    print(Solution().calculate_all_permutations(s))
    g = "DCBA"
    print(Solution().calculate_all_permutations(s))