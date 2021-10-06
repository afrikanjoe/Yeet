class Solution:
    def longestStrChain(self, words):
        
        m = len(words)
        words.sort(key=len)
        visited = [words[0]]
        queue = [[(words[0],0)]]
        longest_chain = 1
        while queue: 
            curr_item = queue.pop(0)
            curr_tup = curr_item[-1]
            curr_word, curr_index = curr_tup[0], curr_tup[1]       
            for k in range(curr_index+1,m):
                if(self.check_pred(curr_word,words[k])):
                    new_ = curr_item[:]
                    new_.append((words[k],k))
                    longest_chain = max(len(new_),longest_chain)
                    queue.append(new_)
                else: 
                    if(words[k] not in visited):
                        visited.append(words[k])
                        queue.append([(words[k],k)])
            #break
        return longest_chain
    
                
                
        
        
    def check_pred(self,str_a,str_b):
        stra_len = len(str_a)
        strb_len = len(str_b)
        if(stra_len == strb_len):
            return str_a == str_b
        if(stra_len < strb_len):
            for i in range(strb_len):
                if(str_b[i] not in str_a):
                    temp_str = str_b[:i] +str_b[i+1:]
                    return temp_str == str_a
        else:
            for i in range(stra_len):
                if(str_a[i] not in str_b):
                    temp_str = str_a[:i] +str_a[i+1:]
                    return temp_str == str_b
        return abs(stra_len - strb_len) == 1
            
                
            
if __name__ == "__main__":
    words = ["a","b","ba","bca","bda","bdca"]
    print(Solution().longestStrChain(words))
    words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    print(Solution().longestStrChain(words))
    words = ["abcd","dbqca"]
    print(Solution().longestStrChain(words))