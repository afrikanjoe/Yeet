class Solution:

    def decompressString(self, string):
        while "[" in string:
            start = 0 
            skip = 0
            end = 0 
            num = ""
            for char in string:
                if(char.isnumeric()):
                    num = num + char
                elif(char=="["):
                    start = string.index(char)
                    break
            for i in range(start+1,len(string)):
                if string[i]=="]" and skip>0:
                    skip-=1
                elif string[i]=="[":
                    skip+=1
                elif string[i]=="]" and skip==0:
                    end = i 
                    break
            string = string[0:start-len(num)] + int(num)*string[start+1:end] + string[end+1:]
        return string 


if __name__ == "__main__":
    s = "3[a2[c]]"
    print(Solution().decompressString(s))
    s = "100[a]"
    print(Solution().decompressString(s))
    s = "3[abc]4[ab]c"
    print(Solution().decompressString(s))