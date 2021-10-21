class Solution:
    def asteroidCollision(self, asteroids):
        remove_indexes = []
        output = asteroids[:]
        i = 0
        count = 0
        while (i < len(output)-1):
            a1 = output[i]
            a2 = output[i+1]
            if(a1>0 and a2<0):
                if(abs(a1)==abs(a2)):
                    output = output[0:i] + output[i+2:]
                elif(abs(a1)>abs(a2)):
                    output = output[0:i+1] + output[i+2:]
                else:
                    output = output[0:i] + output[i+1:]
                i-=1
                i = max(i,0)
            else:
                i+=1
            count+=1
        return output

if __name__ == "__main__":
    inp1 = [5,10,-5]
    inp2 = [8,-8]
    inp3 = [10,2,-5]
    inp4 = [-2,-1,1,2]
    inp5 = [1,-2,-2,1]
    print(Solution().asteroidCollision(inp1))
    print(Solution().asteroidCollision(inp2))
    print(Solution().asteroidCollision(inp3))
    print(Solution().asteroidCollision(inp4))
    print(Solution().asteroidCollision(inp5))