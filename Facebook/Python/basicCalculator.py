class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0 
        num = ''
        operation="+"
        s = s.replace(" ","")
        s = self.get_rid_mults_divides(s)
        for i in s: 
            if(i.isnumeric()):
                num+=i
            elif(operation=="-"):
                stack.append(-int(num))
                operation = i
                num =""
            else:
                stack.append(int(num)) 
                operation = i
                num =""
           
                
        if(operation=="-"):
            stack.append(-int(num))
        else:
            stack.append(int(num)) 
        return sum(stack)
    
    def get_rid_mults_divides(self,s):
        while "*" in s or "/" in s:
            operator=""
            if("*" in s and "/" in s):
                index_m = s.index("*")
                index_d = s.index("/")
                if(index_m<index_d):
                    operator = "*"
                    index = index_m
                else:
                    operator = "/"
                    index = index_d
            elif("*" in s):
                index =  s.index("*")
                operator = "*"
            else:
                index = s.index("/")
                operator = "/"
            left_index = index-1
            right_index = index+1
            left_loop = True
            while left_loop:
                if(left_index-1>=0):
                    if(s[left_index-1].isnumeric()):
                        left_index-=1
                    else:
                        break
                else:
                    break
            left_loop = True
            while left_loop:
                if(right_index+1<len(s)):
                    if(s[right_index+1].isnumeric()):
                        right_index+=1
                    else:
                        break
                else:
                    break
            num1 = int(s[left_index:index])
            num2 = int(s[index+1:right_index+1])
            if(operator=="*"):
                s = s[0:left_index] + str(num1*num2) + s[right_index+1:]
            else:
                s = s[0:left_index] + str(int(num1/num2)) + s[right_index+1:]
          
        return s
                
if __name__ == "__main__":
    s = "4/3*4"
    print(Solution().calculate(s))
                
            
                 
            
        