class Solution:
    def addStrings(self, num1, num2):
        n = min(len(num1),len(num2))
        remainder = 0 
        ret_str = ""
        num1 = list(num1)
        num2 = list(num2)
        
        for i in range(n):
            val1 = int(num1.pop())
            val2 = int(num2.pop())
            suma = remainder + val1 + val2
            if(suma>9):
                new_str = str(suma%10)
                remainder =1 
            else:
                new_str = str(suma)
                remainder = 0 
            ret_str = new_str+ ret_str
            
        finish = None
        if(len(num1)>0):
            finish = num1
        else:
            finish = num2
        
        while finish:
            val1 = int(finish.pop())
            suma = remainder + val1
            if(suma>9):
                new_str = str(suma%10)
                remainder =1 
            else:
                new_str = str(suma)
                remainder = 0 
            ret_str = new_str+ ret_str 
        
        if(remainder>0):
            ret_str = str(remainder) + ret_str
        return ret_str

if __name__ == "__main__":
    num1 = "456"
    num2 = "77"
    print(Solution().addStrings(num1, num2))
    num1 = "11"
    num2 = "123"
    print(Solution().addStrings(num1, num2))