"""
get the nth row of pascal's triangle
"""

class Solution:
    def getRow(self, rowIndex):
        
        if(rowIndex==0):
            return [1]
        if(rowIndex==1):
            return [1,1]
        else:
            
            arr = [1,1]
            for row in range(rowIndex-1):
                new_arr = [1]
                for i in range(len(arr)-1):
                    val = arr[i]+arr[i+1]
                    new_arr.append(val)
                new_arr.append(1)
                arr = new_arr[:]
            return arr

if __name__ == "__main__":
    print(Solution().getRow(10))

