"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde"

"""

class Solution:
    """
        s: str
        words: List[str]
        ret: int
    """
    def numMatchingSubseq(self, s, words):
        # initialize dictionary from s
        s_dict = {}
        s_dict_index = {}
        sub_count = 0  
        index = 0 
        for char in s: 
            s_dict[char] = s_dict.get(char,0)+1
            index_list = s_dict_index.get(char,[])
            if not index_list:
                index_list = []
            index_list.append(index)
            s_dict_index[char] =  index_list
            index+=1
        
        #print(s_dict_index)
        for word in words:
            temp_dict = dict(s_dict)
            temp_dict_index = dict(s_dict_index)
            increment = True
            char_index = 0 
            prev_char = None
            for char in word:
                val = temp_dict.get(char,0)
                if(val<1):
                    increment = False
                    break
                else:
                    temp_dict[char] = val-1
                    if(prev_char):
                        char_index_list = temp_dict_index.get(prev_char)[:]
                        char_index_list_curr = temp_dict_index.get(char)[:]
                        if(max(char_index_list_curr)<min(char_index_list)):
                            increment=False
                            break

                    prev_char = char

            if(increment):
                sub_count+=1
        return sub_count





if __name__=="__main__":
    inp_str,words = "abcdee", ["a","bb","acd","ace"]
    print(Solution().numMatchingSubseq(inp_str,words))

    inp_str,words = "abcdee", ["a","bb","adc","ace"]
    print(Solution().numMatchingSubseq(inp_str,words))

    inp_str = "dsahjpjauf"
    words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    print(Solution().numMatchingSubseq(inp_str,words))