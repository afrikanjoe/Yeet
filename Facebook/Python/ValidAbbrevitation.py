class Solution:
    def validWordAbbreviation(self, word, abbr):
        num =""
        return_str = ""
        abbr_index = 0 
        while abbr_index < len(abbr):
            val = abbr[abbr_index]
            if(val.isnumeric()):
                num = val
                if(int(num)==0):
                    return False
                index = abbr_index
                while index+1<len(abbr):
                    if(abbr[index+1].isnumeric()):
                        num=num+abbr[index+1]
                        index+=1
                        abbr_index+=1
                    else:
                        break
                        
                if(len(word[abbr_index-len(num)+1:abbr_index+int(num)-len(num)+1])<int(num)):
                    return False
                abbr = abbr[:abbr_index-len(num)+1]+word[abbr_index-len(num)+1:abbr_index+int(num)-len(num)+1]+abbr[abbr_index+1:]
            abbr_index+=1
        return abbr == word 

if __name__ == "__main__":
    word = "internationalization"
    abbr = "i12iz4n"
    print(Solution().validWordAbbreviation(word,abbr))
    word = "apple"
    abbr = "a2e"
    print(Solution().validWordAbbreviation(word,abbr))
                    