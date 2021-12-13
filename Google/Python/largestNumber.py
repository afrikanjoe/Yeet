"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""

class Solution:
    def largestNumber(self, nums):
        new_nums = sorted([list(str(i)) for i in nums],reverse=True)
        maxi = 0 
        queue = [[new_nums[:],""]]
        while queue:
            sorted_vals,curr_str = queue.pop(0)
            if(len(sorted_vals)>1):
                l_sorted = sorted_vals[:]
                r_sorted = sorted_vals[:]
                left = l_sorted.pop(0)
                right = r_sorted.pop(1)
                
                tup1 = (l_sorted,curr_str+"".join(left)) 
                queue.append(tup1)
                tup2 = (r_sorted,curr_str+"".join(right))
                queue.append(tup2)
            elif(len(sorted_vals)==1):
                val = sorted_vals.pop()
                tup1 = (sorted_vals,curr_str+"".join(val))
                queue.append(tup1)
            else:
                maxi = max(maxi,int(curr_str))
        return str(maxi)



class customSort(str):
    def __lt__(num1, num2):
        return num1+num2<= num2+num1


class Solution2:
    
    def largestNumber(self, nums):
        l = [str(v) for v in nums]
        l.sort(key=customSort,reverse=True)
        s = ''.join(l)
        if(int(s)==0):
            return "0"
        return s


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(Solution2().largestNumber(nums))
            
            
        