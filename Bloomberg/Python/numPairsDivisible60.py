
# Brute Force
class Solution:
    def numPairsDivisibleBy60(self, time):
        
        ans = []
        visited = []
        count = 0 
        for i in range(len(time)):
            for j in range(len(time)):
                if((i,j) in visited or i==j):
                    continue
                else:
                    visited.append((i,j))
                    visited.append((j,i))
                    if((time[i]+time[j])%60==0):
                        print(time[i],time[j])
                        count+=1
        return count
                

# Optimal Solution Leverages a modulo property
# Which is (a%60) + (b%60) % 60 = 0 
# so either b % 60=0 if a% 60=0 or 
# b % 60 = 60-a % 60, if a%60!=0

class OptimalSolution:
    def numPairsDivisibleBy60(self, time):
        
        remainders = {}
        count = 0 
        for i in time:
            
            if(i%60==0):
                
                val = remainders.get(0,[])
                count+=len(val)
                
            else:
                
                val = remainders.get(60-(i%60),[])
                count+=len(val)
            
            new_val = remainders.get(i%60,[])
            new_val.append(i)
            remainders[i%60]=new_val
        return count

if __name__ == "__main__":
    nums = [60,30,150,100,40,80,120]
    print(OptimalSolution()).numPairsDivisibleBy60(nums)