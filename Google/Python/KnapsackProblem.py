"""

    Refresher on the knapsack problem. Problem taken from 
    https://www.cs.cmu.edu/~avrim/451f09/lectures/lect1001.pdf

"""


class Solution: 
    def knapsack(self,values,weights,capacity):

        yx = sorted(zip(weights,values))
        values = [x[1] for x in yx]
        weights = [x[0] for x in yx]

        print(values,weights)
        
        arr = []
        for i in range(len(values)+1):
            arr.append([0]*(capacity+1))

        ### go through the array and fill in the values
        for i in range(1,len(values)+1):
            for j in range(1,(capacity+1)):
                # get the weight and value
                wi = weights[i-1]
                vi = values[i-1]
                
                # check if we can put in this index 
                if(j>=wi):
                    col = j-wi
                    col_above = arr[i-1][j]
                    remaining_capacity = arr[i-1][col]
                    arr[i][j] = max(vi+remaining_capacity,col_above)
                else:
                    arr[i][j] = arr[i-1][j]

        # for i in arr:
        #     print(i)
        
        selected_items=self.get_items(arr,values,weights)
        

        return arr[-1][-1]

    def get_items(self,arr,values,weights):
        m = len(arr)
        n = len(arr[0])-1
        selected_items = []
        for i in range(m-1,0,-1):
            if(arr[i-1][n]==arr[i][n]):
                continue
            else:
                selected_items.insert(0,i-1)
                n = n - weights[i-1]


        weight = sum([weights[i] for i in selected_items])
        print("selected items:",selected_items,"weight:",weight, "value:",arr[-1][-1])
        return selected_items


if __name__=="__main__":
    values = [7,9,5,12,14,6,12]
    weights = [3,4,2,6, 7, 3,5]
    capacity = 15
    print(Solution().knapsack(values,weights,capacity))

    values = [2,3,1,4]
    weights = [3,4,6,5]
    capacity = 8
    print(Solution().knapsack(values,weights,capacity))