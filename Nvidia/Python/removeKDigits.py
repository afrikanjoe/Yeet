class Solution:
    def removeKdigits(self, num, k):
        len_ans = len(num) - k
        if(len_ans==0):
            return "0"
        min_digit = None
        
        queue = [num]
        while queue: 
            new_num = queue.pop(0)
            if(len(new_num)==len_ans):
                
                if(min_digit!=None):
                    if(not new_num):
                        min_digit = min(min_digit,0)
                    else:
                        min_digit = min(min_digit,int(new_num))
                else:
                    if(not new_num):
                        min_digit = 0
                    else:
                        min_digit = int(new_num)
            else:
                for i in range(len(new_num)):
                    new_s = new_num[0:i] + new_num[i+1:]
                    if(new_s not in queue):
                        queue.append(new_s)
        return str(min_digit)

class OptimalSolution:
    def removeKdigits(self, num, k):
        numStack = []
        
        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
            
        while k:
            numStack.pop()
            k-=1
        if(not numStack):
            return "0"
        return str(int("".join(numStack)))

if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(OptimalSolution().removeKdigits(num,k))
        