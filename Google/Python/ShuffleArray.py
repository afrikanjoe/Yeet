class Solution:

    def __init__(self, nums):
        self.orig = nums[:]
        self.arr = nums
        self.seed =10
        

    def reset(self):
        self.arr = self.orig[:]
        return self.arr
        

    def shuffle(self):
        added = []
        arr = []
        indices = self.uniform_range(0,len(self.orig),size=10*len(self.orig),seed=self.seed)
        index = 0 
        while len(added)<len(self.orig) and index < len(indices):
            ind = indices[index]
            if(ind in added):
                index +=1
            else:
                added.append(ind)
                arr.append(self.arr[ind])
        print(indices)
        self.arr = arr
        self.seed*=2
        return self.arr
                
        
        
        return self.arr
    
        
        
    def uniform_range(self,low,high,seed=123456789,size=1):
        ls = self.pseudo_uniform(seed=seed,size=size)
        answ = [int(low+((high-low)*i))   for i in ls]
        return answ
        
    def pseudo_uniform(self,mult=16807,mod=(2**31)-1, seed=123456789,size=1):
        U = [0]*size
        x= (seed*mult+1) % mod
        U[0] = x/mod
        for i in range(1,size):
            x = (x*mult+1)%mod
            U[i] = x/mod
        return U


# Fisher Yates shuffle with built in library (boring)
class Solution2:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array