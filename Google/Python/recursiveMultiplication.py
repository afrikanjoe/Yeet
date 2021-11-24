"""
write a function that recursively multiplies two numbers without using the * operator
"""

class Solution:
    def recursiveMultiply(self,a,b):
        negative = False
        if(a==0 or b==0):
            return 0
        if((a<0 and b>0) or (a>0 and b<0)):
            negative = True

        def recursive_helper(a,b):
            curr_sum = a
            if(b==1):
                return a
            else:
                curr_sum+=recursive_helper(a,b-1)

            return curr_sum
        
        if(negative):
            return - recursive_helper(abs(a),abs(b))
        else:
            return recursive_helper(abs(a),abs(b))

if __name__ == "__main__":
    print(Solution().recursiveMultiply(-3,0))


