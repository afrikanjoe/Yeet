"""
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.


Example 1: 
-------------------------------------------------------------
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
-------------------------------------------------------------
Input: ["aa","bb","ccc"]
[["aa","bb"],["ccc"]]


The key behind this question was generating semi-unique keys, my intution was almost correct
but not quite.
"""

class Solution:
    def groupStrings(self, strings):
        string_order = {}
        res = []
        def calc_string_order(string):
            val = ""
            for i in range(len(string)-1):
                val+= str((ord(string[i+1]) - ord(string[i])) % 26)
            return val 
        
        for i in strings:
            str_len = len(i)
            num = calc_string_order(i)
            val = string_order.get(str_len,[])
            if(len(val)==0):
                string_order[str_len] = [[i]]
            else:
                added = False
                for ls in val:
                    if(calc_string_order(ls[0])==num):
                        ls.append(i)
                        added = True
                        break
                if(not added):
                    val.append([i])
                    string_order[str_len] = val 
         
        for i in sorted(string_order.keys()):
            for ls in string_order[i]:
                res.append(ls)
        return res
        

if __name__ == "__main__":
    inp = ["aa","bb","ccc"]
    print(Solution().groupStrings(inp))
    inp = ["abc","bcd","acef","xyz","az","ba","a","z"]
    print(Solution().groupStrings(inp))