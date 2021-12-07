from collections import Counter

class Solution:
    def countAndSay(self, n):
        
        if(n==1):
            return "1"
        else:
            
            val = self.countAndSay(n-1)
            stack = []
            num = ""
            for i in val:
                if(len(num)==0):
                    num=num+i
                else:
                    if(i==num[-1]):
                        num = num + i
                    else:
                        stack.append(num)
                        num=i
            if(len(num)>0):
                stack.append(num)
            new_str = ""
            for n in stack:
                c = Counter(n)
                keys = list(c.keys())
                for key in keys:
                    temp = str(c[key])+key
                    new_str = new_str + temp
            return new_str

if __name__ == "__main__":
    print(Solution().countAndSay(7))