from functools import lru_cache
class Solution:

    # top down solution 
    def numSquaresv1(self, n):
        
        @lru_cache(maxsize=None)
        def numSquaresHelper(n,count):
            if(n==0):
                return count
            else:
                counts = []
                for i in range(int(math.sqrt(n)),0,-1):
                    counts.append(numSquaresHelper(n-(i**2),count+1))
                return min(counts)
        
        return numSquaresHelper(n,0)

    # better dfs but not quite the one 
    def numSquaresv2(self, n):
        queue = [(n,0)]
        visited = []
        while queue:
            val,count = queue.pop(0)
            visited.append(val)
            if(val==0):
                return count
            for i in range(int(math.sqrt(val)),0,-1):
                
                new_val =val-(i**2)
                if new_val>=0 and new_val not in visited:
                    queue.append((new_val,count+1))
                
        return -1

    # optimal solution is genius
    def numSquares(self, n):
        
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
        
       
        level = 0
        queue  = {n}
        while queue:
            level +=1
            
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if(remainder==square_num):
                        return level
                    elif(remainder<square_num):
                        break
                    else:
                        next_queue.add(remainder - square_num)
                        
            queue = next_queue
        return level


if __name__ == "__main__":
    print(Solution().numSquares(101))