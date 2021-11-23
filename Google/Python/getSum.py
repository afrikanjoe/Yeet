"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

class Solution:
    # the first thing to notice is that this problem can be solved in two cases
    # x+y, x>0 y>0 x<0, y < 0 
    # x-y , x>y 
    def getSumBadLol(self, a, b):


        if((a>=0 and b>=0) or (a<0 and b<0)):
            negative = False
            if(a<0 and b<0):
                negative = True
            a = abs(a)
            b = abs(b)
            carry = b
            y = a
            # keep looping while we have a carry, this is actually pretty sick
            while carry:
                val = y ^ carry 
                carry = (y & carry)<<1
                y = val
            if(negative):
                return -y
            return y
        else:
            negative = False
            if(b<0 and abs(b)>abs(a)):
                #print("negative",b,a)
                negative = True
                y = abs(b)
                borrow = abs(a)
            elif(a<0 and abs(b)>abs(a)):
                #print("positive",b,a)
                y = abs(b)
                borrow = abs(a)
            elif(a<0 and abs(a)>abs(b)):
                #print("positive",b,a)
                y = abs(a)
                borrow = abs(b)
                negative = True
            else:
                y = abs(b)
                borrow = abs(a)
            while borrow:
                val = y ^ borrow
                borrow = (~y & borrow)<<1
                y = val

            if(negative):
                return -y
            else:
                return y 
            #return val

    def getSum(self,a,b):
        x, y = abs(a), abs(b)
        if(x<y):
            return self.getSum(b,a)
        
        negative = False
        if(a<0):
            negative = True

        if(a*b>=0):
            while y:
                temp = y ^ x
                y = (x & y) << 1
                x = temp 
        else:
            while y:
                temp = y^x
                y = ((~x) & y) << 1
                x = temp 
        
        if(negative):
            return -x 
        else:
            return x
        

        
if __name__ == "__main__":
    a = 10 
    b = 14
    print(Solution().getSum(a,b))

    a = 33 
    b = 15
    print(Solution().getSum(a,b))

    a = -5 
    b = -3
    print(Solution().getSum(a,b))

    a = 3
    b = -10 
    print(Solution().getSum(a,b))

    a = -3
    b = 10 
    print(Solution().getSum(a,b))


    a = -1
    b = 0 
    print(Solution().getSum(a,b))
    
