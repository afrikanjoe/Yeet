class Solution:
    def getCollisionTimesPat(self, cars):
        res = []
        
        for i in range(len(cars)-1):
            
            car1 = cars[i]
            car2 = cars[i+1]
            
            if(car2[1]<car1[1]):
                res.append ((car2[0]-car1[0])/(car1[1]-car2[1]))
                car1[1] = car2[1]
            else:
                res.append(-1)
                
        print(res)
        print(cars)
        for i in range(len(cars)-1):
            if(res[i]<0):
                car1 = cars[i]
                car2 = cars[i+1]
                if(car2[1]<car1[1]):
                    res[i]= ((car2[0]-car1[0])/(car1[1]-car2[1]))
        res.append(-1)
        return res


    def getCollisionTimes(self,cars):
        stack = []
        res = [-1]*len(cars)

        for i in range(len(cars)-1, -1, -1):
            
            ccP, ccS = cars[i]
            
            while stack:
                
                top = cars[stack[-1]]
                
                
                if top[1] >= ccS or (top[0] - ccP) / (ccS-top[1]) >= res[stack[-1]] > 0:
                    stack.pop()
                else:
                    break
                    
            
            if stack:
                top = cars[stack[-1]]
                collisonT = (top[0] - ccP) / (ccS-top[1])
                res[i] = collisonT
            
            stack.append(i)
        
        return res




if __name__ == "__main__":
     cars = [[1,2],[2,1],[4,3],[7,2]]
     print(Solution().getCollisionTimes(cars))

     cars = [[3,4],[5,4],[6,3],[9,1]]
     print(Solution().getCollisionTimes(cars))