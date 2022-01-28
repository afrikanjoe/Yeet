"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.

"""

class WordDictionary:

    def __init__(self):
        
        self.length_dict = {}
        self.word_dict = {}
        

    def addWord(self, word):
        
        self.word_dict[word] = word
        val = self.length_dict.get(len(word),[])
        val.append(word)
        self.length_dict[len(word)]=val
        

    def search(self, word):
        if("." not in word):
            return self.word_dict.get(word,"") == word
        else:
            same_lens = self.length_dict.get(len(word),[])
            
            for word2 in same_lens:
                valid = True
                for i in range(len(word)):
                    
                    letter = word[i]
                    letter2 = word2[i]
                    if(letter=="."):
                        continue
                    elif(letter!=letter2):
                        valid = False
                        break
                if(valid):
                    return True
            return False