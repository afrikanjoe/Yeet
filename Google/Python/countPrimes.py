"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""


import math 
class Solution:
    def countPrimes(self, n):
        count_primes = 0
        for i in range(2,n):
            if(self.check_primes(i)):
                count_primes+=1
        return count_primes
        
        
    def check_primes(self,n):
        for i in range(2,int(sqrt(n))+1):
            
            if(n%i==0):
                return False
        return True

if __name__ == "__main__":
    n = 20
    print(Solution().countPrimes(n))