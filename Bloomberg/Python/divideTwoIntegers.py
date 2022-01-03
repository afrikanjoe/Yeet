"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. 
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -23

"""

class Solution:
    def divide(self, dividend, divisor):
        sign = 0 
        if(dividend< 0 and divisor>0):
            sign=-1
        elif (divisor<0 and dividend>0):
            sign=-1
            
        
        count = 0 
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend>0 and dividend>=divisor:
            dividend-=divisor
            count+=1
        
        if(sign<0):
            return -count
        else:
            return count


class OptimalSolution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 0 
        if(dividend< 0 and divisor>0):
            sign=-1
        elif (divisor<0 and dividend>0):
            sign=-1
            
        
        divisors  = []
        subtracts = []
        
        
        double=1
        dividend = abs(dividend)
        divisor = abs(divisor)
        value = divisor
        
        # keep doubling the divisor until you 
        # get the integer larger than the dividend
        while value <= dividend:
            subtracts.append(value)
            divisors.append(double)
            double=double+double
            value = value + value
      
        index = len(divisors)-1
        count = 0 
        while dividend>0 and index>=0:
            if(dividend>=subtracts[index]):
                dividend -=subtracts[index]
                count+=divisors[index]
            index-=1
            
        if(abs(count)==2**31):
            if(sign==0):
                count = 2**31-1
        if(sign<0):
            return -count
        else:
            return count

if __name__ == "__main__":
    dividend = 10
    divisor = 3
    print(OptimalSolution().divide(dividend,divisor))
    dividend = 7
    divisor = -3
    print(OptimalSolution().divide(dividend,divisor))