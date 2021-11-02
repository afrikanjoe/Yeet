class Solution:
    def isAlienSorted(self, words, order):
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]]=i
            
        for i in range(len(words)-1):
            
            valid = self.compare_words(words[i],words[i+1],order_dict)
            if(valid):
                return False
            
        return True

    def compare_words(self,word1,word2,order_dict):
        if(word1==word2):
            return False
        
        min_len = min(len(word1),len(word2))
        if(word1[:min_len]==word2[:min_len]):
            if(len(word2)<len(word1)):
                return True
        
        for i in range(min_len):
            val1 = order_dict[word1[i]]
            val2 = order_dict[word2[i]]
            if(val1==val2):
                continue
            if(val2<val1):
                return True
            else:
                return False


if __name__ == "__main__":
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(Solution().isAlienSorted(words,order))