"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) 
and cannot have leading zeros.For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312"
 and "192.168@1.1" are invalid IP addresses. Given a string s containing only digits, return all possible valid IP addresses 
 that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. 
You may return the valid IP addresses in any order.


"""

class Solution:
    def restoreIpAddresses(self, s):
        
        
        queue = [s]
        ans = []
        while queue:
            curr_str = queue.pop()
            if(len(curr_str.split("."))==4):
                if(self.valid_ip(curr_str)):
                    ans.append(curr_str)
            elif(len(curr_str.split("."))<4):
                dot_index = curr_str.rfind(".")
                for i in range(dot_index+2,len(curr_str)):
                    new_str = curr_str[0:i] + "." + curr_str[i:]
                    queue.append(new_str)
        return ans
    
    def valid_ip(self,ls):
        
        for i in ls.split("."):
            if(str(int(i))==i and int(i)>=0 and int(i)<=255):
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))
        
        
                